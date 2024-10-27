from qlab_interface import Interface
#Allows us to convert integers to roman numerals, if there are more than 16 scenes
import roman

def _fix_scene_numbers(interface):
    last_cue_no = None
    #This code block iterates through the queues till either it reaches the last queue or the current queue is none
    #So it will return none
    while True:
        cue_no = interface.select_next_cue()
        if cue_no and '--' in cue_no:
            if cue_no == last_cue_no:
                return
            last_cue_no = cue_no

            act, rest = cue_no.split('--')
            act = int(act)
            scene, rest = rest.split('.', 1)
            scene = int(scene)
            numeral = roman.toRoman(scene)
            new_no = '{}-{}  {}'.format(act, numeral, rest)
            interface.set_cue_property('selected', 'number', new_no)

if __name__ == '__main__':
    interface = Interface()
    interface.client.send_message('/select/4.12.0')
    _fix_scene_numbers(interface)

