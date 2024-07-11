from qlab_interface import Interface

#Constant values for the show
FIRST_CUE = 0
LAST_CUE = 9999


def populate_notes(interface):
    while True:
        cue_no = interface.get_cue_property('selected', 'number')
        if cue_no == LAST_CUE:
            return
        caption_type = interface.get_cue_property('selected', 'type')
        print('caption type', caption_type)
        notes = interface.get_cue_text('selected') if caption_type == 'Titles' else interface.get_cue_property('selected', 'name')
        print(notes)
        if notes:
            interface.set_cue_property('selected', 'notes', notes)
        interface.client.send_message('/select/next')

if __name__ == '__main__':
    interface = Interface()
    interface.client.send_message('/select/{}'.format(FIRST_CUE))
    populate_notes(interface)

