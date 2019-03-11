windows=$(tmux list-windows | awk '{print $2;}' | grep -P '^P')
# Delete all windows
for x in $windows; do
    y=$(sed 's/-$//' <<< "$x")
    tmux kill-window -t $y
done
tmux select-window -t :0
