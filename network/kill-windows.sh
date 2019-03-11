windows=$(tmux list-windows | awk '{print $2;}' | grep -P '^P')
# Delete all windows
for x in $windows; do
    tmux kill-window -t $x
done
tmux select-window -t :0
