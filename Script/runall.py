import argparse
import subprocess
import sys
from pathlib import Path
from pack_paths import PACK_DIRECTORY_NAMES

scriptDir = Path(__file__).resolve().parent

useDownloader = True
extraSteps = True

jeLangs = [
    "bg_bg", "cs_cz", "da_dk", "de_de", "el_gr", "en_gb", "en_au",
    "en_ca", "en_nz", "en_us", "es_es", "es_mx", "et_ee", "fi_fi", 
    "fr_ca", "fr_fr", "hu_hu", "id_id", "it_it", "ja_jp", "ko_kr", 
    "no_no", "nl_nl", "pl_pl", "pt_br", "pt_pt", "ru_ru", "sk_sk", 
    "sv_se", "tr_tr", "uk_ua", "zh_cn", "zh_tw",
]
beLangs = [
    "bg_BG", "cs_CZ", "da_DK", "de_DE", "el_GR", "en_GB", "en_GB",
    "en_GB", "en_GB", "en_US", "es_ES", "es_MX", "et_EE", "fi_FI", 
    "fr_CA", "fr_FR", "hu_HU", "id_ID", "it_IT", "ja_JP", "ko_KR", 
    "nb_NO", "nl_NL", "pl_PL", "pt_BR", "pt_PT", "ru_RU", "sk_SK", 
    "sv_SE", "tr_TR", "uk_UA", "zh_CN", "zh_TW",
]

parser = argparse.ArgumentParser()
parser.add_argument(
    "downloader",
    nargs="?",
    type=str.lower,
    choices=("true", "false"),
    default=None,
    help="Download language inputs before building (default: true).",
)
parser.add_argument(
    "--pack",
    type=str.lower,
    choices=("all", *PACK_DIRECTORY_NAMES),
    default="all",
    help="Select one profile, or build both (default: all).",
)
args = parser.parse_args()
if args.downloader is not None:
    useDownloader = args.downloader == "true"
packs = list(PACK_DIRECTORY_NAMES) if args.pack == "all" else [args.pack]

if useDownloader:
    print("Executing the downloader script...")
    subprocess.run([sys.executable, str(scriptDir / "downloader.py")], check=True)
    print("Download script completed.\n")

for pack in packs:
    print(f"\nBuilding the {pack} profile...")
    print("Now executing the mapper script...")
    subprocess.run(
        [sys.executable, str(scriptDir / "mapper.py"), "--pack", pack],
        check=True,
    )
    print("Mapper script completed.")

    if extraSteps:
        if pack == "bedrockflavor":
            print("\nNow executing the spawn egg adding script...")
            subprocess.call(
                [sys.executable, str(scriptDir / "spawn-egg-adder.py"), "--pack", pack]
            )
            print("Spawn egg adding script completed.")
        print("Now executing the extra mapping cleanup...")
        subprocess.call(
            [sys.executable, str(scriptDir / "clean-extra-mappings.py"), "--pack", pack]
        )
        print("Extra mapping cleanup completed.")

    print("Now executing the porting script for language pairs...")
    porterArgs = [sys.executable, str(scriptDir / "porter.py"), "--pack", pack]
    if jeLangs or beLangs:
        porterArgs.extend([",".join(jeLangs), ",".join(beLangs)])
    subprocess.run(porterArgs, check=True)
    print("Porting script completed.")
