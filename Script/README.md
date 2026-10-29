## Scripts

* `runall.py` - Runs mapping and porting for both profiles, with an optional shared input download.
* `downloader.py` - Downloads the latest stable Java Edition language files, all stable Bedrock `.lang` files, and Estonian from the latest language-pack release.
* `mapper.py` - Creates profile-specific CSV key mappings by comparing English Java and Bedrock strings.
* `porter.py` - Uses the selected profile's source data to create Java Edition `.json` files.

## Files

* `Input/` - Downloaded Java `.json` and Bedrock `.lang` language files.
* `Extra-BedrockFlavor/` - BedrockFlavor mapping CSVs and configuration, including `source-en_us.json`, `overrides.json`, `prefixes.json`, and locale-specific `extra-*.json` files.
* `Extra-Bedrocking/` - Bedrocking source strings, profile-scoped CSV mappings, and locale-specific `extra-*.json` files.
* Each profile's `mappings.csv` is generated automatically; `extra-mappings.csv` contains additional human-created mappings.
* `Output-BedrockFlavor/` and `Output-Bedrocking/` - Generated Java Edition `.json` language files for each profile.
* `requirements.txt` - Required Python libraries for running all scripts used in the project.

## How to use

1. [Download Python](https://www.python.org/downloads/)
2. Install the requirements with PIP: `python -m pip install -r requirements.txt`
3. Run `python runall.py` to download shared inputs and build both profiles.
   * Add `false` to skip downloading and use local files in `Input/`, e.g. `python runall.py false`. The default is `true`.
   * Add `--pack bedrockflavor` or `--pack bedrocking` to build only one profile. For example, `python runall.py false --pack bedrocking` builds Bedrocking from local inputs.
4. Find generated language files in the matching `Output-*` directory.

Both profiles use the shared Bedrock `.lang` and Java `.json` files in `Input/`. BedrockFlavor ports generic Bedrock mappings and supplements them with its source strings and locale extras. Bedrocking generates and consumes mappings only for keys in its source strings, then applies its locale extras; generic vanilla mappings are filtered out.
- `source-en_us.json` supplies profile-specific English strings and allowed mapping targets; for Bedrocking these are the base output entries for `en_us`.
- `extra-*.json` adds or replaces strings for a specific Java language after generic mapping.
- `overrides.json` replaces output values.
- `prefixes.json` adds prefixes to mapped output values.
Language files are paired automatically when their locale codes match, ignoring case; Bedrock languages without a matching Java language file are skipped.

## Credit

Code and Estonian translations forked from https://github.com/Madis0/mc-language-porter :)