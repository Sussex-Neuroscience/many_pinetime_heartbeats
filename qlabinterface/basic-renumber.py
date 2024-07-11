from qlab_interface import Interface

def _fix_simple_cue_numbers(interface):
    while True:
        cue_no = interface.get_cue_property('selected', 'number')
        print(cue_no)
        if cue_no:
            act, scene, number = map(int, (cue_no[:1], cue_no[1:3], cue_no[3:]))
            if act > 4:
                break
            new_no = '{}.{}.{}'.format(act, scene, number)
            interface.set_cue_property('selected', 'number', new_no)

        interface.client.send_message('/select/next')

if __name__ == '__main__':
    interface = Interface()
    interface.client.send_message('/select/40818')
    _fix_simple_cue_numbers(interface)

