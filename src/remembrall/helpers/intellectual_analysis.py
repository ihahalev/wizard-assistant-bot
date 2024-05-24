from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter

# Need to install the package: pip install prompt_toolkit
commands = WordCompleter([
    "close", "exit", "hello","all-contacts", "add-contact", "show-contact", "change-contact",
    "remove-contact", "change-phone", "remove-phone", "add-birthday", "change-birthday",
    "birthdays", "add-email", "change-email", "add-address", "change-address",
    "remove-address", "all-notes", "add-note", "show-note", "change-note", "remove-note",
    "change-title", "add-tag", "remove-tag", "change-tag", "help" ], ignore_case=True)
session = PromptSession(completer=commands)