# -*- coding: utf-8 -*-
from evernote.api.client import EvernoteClient
from evernote.edam.notestore.ttypes import NoteFilter

from config import config_items

    
if __name__ == '__main__':
    client = EvernoteClient(
        token=config_items['EVERNOTE_PERSONAL_TOKEN'],
        sandbox=config_items['SANDBOX'],
    )
    note_store = client.get_note_store()

    notebooks = note_store.listNotebooks()
    for notebook in notebooks:
        filter = NoteFilter()
        filter.notebookGuid = notebook.guid
        noteList = note_store.findNotes(
            config_items['EVERNOTE_PERSONAL_TOKEN'],
            filter,
            0,
            50,
            )
        notes_guid = [note.guid for note in noteList.notes]
        print('%s - %s' % (notebook.guid, notebook.name))
        print('%s - %s' % ('Список заметок', notes_guid))
