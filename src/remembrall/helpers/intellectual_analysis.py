import re
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter

# Need to install the package: pip install prompt_toolkit
commands = WordCompleter([
        "close", "exit", "hello", "help",
        "all-contacts", "add-contact", "show-contact", "change-contact", "remove-contact",
        "change-phone", "remove-phone",
        "add-birthday", "change-birthday","birthdays",
        "add-email", "change-email", "remove-email",
        "add-address", "change-address", "remove-address",
        "all-notes", "add-note", "show-note", "change-note", "remove-note",
        "change-title",
        "add-tag", "remove-tag", "change-tag", "sort-tags", "find-content"
    ],
    ignore_case=True,
    pattern=re.compile(r"^([a-zA-Z0-9_.\-]+|[^a-zA-Z0-9_.\s\-]+)"),
)

session = PromptSession(completer=commands)
