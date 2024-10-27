from qlab_interface import Interface


def _fix_act_numbers(interface):
    last_cue_no = None
    while True:
        cue_no = interface.get_cue_property('selected', 'number')
        if cue_no and cue_no != last_cue_no:
            last_cue_no = cue_no
            act, rest = cue_no.split('.', 1)
            act = int(act)
            new_no = f'{act}--{rest}'
            interface.set_cue_property('selected', 'number', new_no)

        interface.client.send_message('/select/next')

if __name__ == '__main__':
    interface = Interface()
    interface.client.send_message('/select/4.12.0')
    _fix_act_numbers(interface)

