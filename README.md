# High Time Cymbaline

## Running

1. Clone this repository first by issuing `git clone https://github.com/madziejm/high-time-cymbaline` command.
2. Download *Poleval vectors* by issuing `make` command. They are needed to generate your haiku.
3. Only generating haiku is available via CLI currently. Run the bot this way: `python3 run.py`. Wait some time for evauating magical stuff. After prompt `>` shows on your computer, the bot is ready. You can type `napisz mi haiku o: pies` to generate haiku about dogs for example.

## Modules

1. *Controller Module* – dispatches the given input to the Response Modules and sends the input to the View Module. Keeps the context to use it later on.
2. Response Modules
   * Create a haiku or limerick of random words sequence
   * Search for an appriopriate response in Poleval Corpus
   * Search for an appriopriate response in Polish Literature Corpus
   * Find an appriopriate quote in Wikiquote database
3. *View Module* - >>REPL<<-style or GUI module

## Proposed implementation (bound to be changed)

- `DataProvider` - @miloczek - loading, storing and answering questions about requested corpora/wikiquotes.
- `LanguageToolkit` - @PaulinaLa - implements text operators and transformators: word tagging, syllables counting, rhyme checking.
- `Haiku(Generator)`, `Generator` - @madziejm - allows for creation of haikus based on given keywords and Generator _Schema_. 
- `Interaction` - @mkochanowski - a single exchange between the user and the Bot, responsible for choosing the most likely answer from the set of generated ones.
- `Bot` - main module - uses previously defined classes to process user input and return a response.  
- `TelegramConnector(BaseConnector)`, `BaseConnector` - @krzysztofnyczka - exposes the Bot to the outside world.

## Contributing

To contribute to the project, please create a new branch from `master`:

```
git checkout -b my-name-of-the-branch master
```

Your commit message should briefly summarize the changes (if possible) in plain English. To learn how to write a proper commit message, check out [this article](https://juffalow.com/other/write-good-git-commit-message).

> **Note**: You should not commit directly to the `master` branch.  

When ready, create a new pull request compared with the `master` branch set as a base branch.
