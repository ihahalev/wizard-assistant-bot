format = "%d.%m.%Y"
created_at_format = '%d.%m.%Y.%H.%M'

storage_link = "src/storage"
supported_files = {
    "b": ".pkl",
    "j": ".json"
}

commands = [['Command', 'Parameters', 'Description'],
                ['all-contacts', '', 'list all information about contacts'],
                ['add-contact', '[Name] [Phone]','create new user with phone in adress book'],
                ['show-contact', '[Name]','show contact with all info'], 
                ['change-contact', '[Name] [New_name]', 'change contact name'],
                ['remove-contact', '[Name]', 'remove contact from adress book'],
                ['change-phone', '[Name] [Phone] [new_Phone]', 'change contact phone'],
                ['remove-phone', '[Name] [Phone]', 'remove contact phone'],
                ['add-email', '[Name] [Email]', 'add contact email'],
                ['change-email', '[Name] [Email] [new_Email]', 'change contact email'],
                ['remove-email', '[Name] [Email]', 'remove contact email'],
                ['add-address', '[Name] [Address]', 'add contact address'],
                ['change-address', '[Name] [Address] [New Addres]', 'change contact address'],
                ['add-birthday', '[Name] [Birthday]', 'add contact birthday'],
                ['change-birthday', '[Name]' '[Birthday]' '[NewBirthday]', 'change contact birthday'],
                ['birthdays', '[int]', 'shows upcoming birthdays from today for next [int] days'],
                ['add-note', '[Title]' '[Note text]', 'Add a note to Note Book'],
                ['show-note', '[Title]', 'show note with all info'],
                ['all-notes', '', 'show all notes with all info'],
                ['change-note', '[Title] [Note]', 'change note text'],
                ['remove-note', '[Title]', 'remove note'],
                ['change-title', '[Title] [New Title]', 'change note title'],
                ['add-tag', '[Title] [Tag]', 'add note tag'],
                ['remove-tag', '[Title]', 'remove note tag'],
                ['sort-tags', '[Tag1] [Tag2] ...', 'sort all Notes with tag'],
                ['find-content', '[Content]', 'list all Notes with content'],
                ['close, exit', '', 'exit the bot'],
                ['help', '', 'list all bot commands']]
