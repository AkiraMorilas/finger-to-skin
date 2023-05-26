# finger-to-skin
Takes skin elements, and arranges them per-finger, and generates an osumania skin.
The supported keycounts are all sensible **keyboard** keycounts, so
- 1K to 10K
- 13K in 3K7K3K arrangement(which cannot have keybinds changed, but can actually be mapped with notepad editing)
- 17K in 4K9K4K arrangement(same as above)
- 18K in 4K10K4K arrangement

This script doesn't generate anything for controller-oriented keycounts like 12K(10K2S), mainly because I don't play controller games like BMS anymore, but also because scratching support is buggy in stable and non-existent in lazer(which I use).

This script **should** be centering the stage correctly, but I'm not sure because lazer mania is a buggy mess and I can't get stable to work in Wine.
Also keep in mind that barlines cannot be hidden in lazer *by design*(see https://github.com/ppy/osu/issues/19611)

# TODO:
I want to eventually just generate the whole skin.ini
- figure out JudgementLine, NoteBodyStyle and all the non-mania specific stuff
- key images
- togglable advanced mode where you choose every image(right now same image is used for note, LN head, LN body and LN tail)

I also want to do this with soundsphere(https://github.com/semyon422/soundsphere) skins but I might make that a separate script.
