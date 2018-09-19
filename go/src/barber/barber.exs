defmodule BarberShop do
  @name :barber_shop
  @num_chairs 3

  def open do
    shop_pid = spawn(__MODULE__, :loop, [])
    :global.register_name(@name, shop_pid)
    Barber.register(shop_pid)
  end

  # add one or more customers to shop
  def add(customers) when is_list(customers), do: customers |> Enum.map(&add/1)
  def add(customer), do: send(self_pid, {:add, customer})

  # check status of shop
  def status?, do: send(self_pid, {:shop_status})

  # check status of barber
  def barber?, do: send(self_pid, {:barber_status})

  def loop(barber_pid \\ nil, in_chair \\ nil, waiting \\ []) do
    receive do
      {:shop_status} ->
        IO.puts("in chair: #{inspect(in_chair)}")
        IO.puts("waiting: #{inspect(waiting)}")
      {:barber_status} ->
        cond do
          in_chair ->
            IO.puts("barber is currently cutting hair for #{in_chair}")
          true ->
            IO.puts("barber fell asleep")
        end
      {:barber_done} ->
        IO.puts("barber is finished cutting hair for #{in_chair}")
        case waiting do
          [next|remaining] ->
            send(barber_pid, {:cut, next})
            loop(barber_pid, next, remaining)
          [] ->
            loop(barber_pid, nil, [])
        end
      {:add, customer} ->
        cond do
          chair_empty?(in_chair) ->
            send(barber_pid, {:cut, customer})
            loop(barber_pid, customer, waiting)
          shop_full?(waiting) ->
            IO.puts("shop is full, customer is leaving ...")
          true ->
            IO.puts("customer is sitting down")
            loop(barber_pid, in_chair, [customer|waiting])
        end
      {:register_barber, barber_pid} ->
        IO.puts("registering barber: #{inspect(barber_pid)}")
        loop(barber_pid, in_chair, waiting)
    end
    loop(barber_pid, in_chair, waiting)
  end

  # boolean helpers
  defp chair_empty?(in_chair), do: is_nil(in_chair)
  defp shop_full?(waiting), do: Enum.count(waiting) >= @num_chairs

  # lookup self pid
  defp self_pid, do: :global.whereis_name(@name)
end

defmodule Barber do
  @time_per_cut 3_000
  @time_until_bored 30_000

  def register(shop_pid) do
    barber_pid = spawn(__MODULE__, :loop, [shop_pid])
    send(shop_pid, {:register_barber, barber_pid})
  end

  def loop(shop_pid) do
    receive do
      {:cut, customer} ->
        IO.puts("cutting hair for #{customer}")
        :timer.sleep(@time_per_cut)
        send(shop_pid, {:barber_done})
      after @time_until_bored ->
        IO.puts("yawn. not much to do around here...")
    end
    loop(shop_pid)
  end
end