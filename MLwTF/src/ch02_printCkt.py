from tensorflow.python.tools import inspect_checkpoint as inch
inch.print_tensors_in_checkpoint_file('./spikes.ckpt', '', all_tensor_names='', all_tensors=True)
