from pathlib import Path


DEFAULT_PACK = "bedrockflavor"
PACK_DIRECTORY_NAMES = {
    "bedrockflavor": "BedrockFlavor",
    "bedrocking": "Bedrocking",
}


def add_pack_argument(parser, default=DEFAULT_PACK):
    parser.add_argument(
        "--pack",
        choices=tuple(PACK_DIRECTORY_NAMES),
        default=default,
        help="Select the resource pack profile.",
    )


def get_pack_paths(script_dir, pack=DEFAULT_PACK):
    pack_name = pack.casefold()
    if pack_name not in PACK_DIRECTORY_NAMES:
        choices = ", ".join(PACK_DIRECTORY_NAMES)
        raise ValueError(f"Unknown pack '{pack}'. Choose from: {choices}.")

    directory_name = PACK_DIRECTORY_NAMES[pack_name]
    return (
        Path(script_dir) / f"Extra-{directory_name}",
        Path(script_dir) / f"Output-{directory_name}",
    )