# ComfyUI-CyberRealistic-Pony

Custom nodes for generating prompts for Cyber Realistic Pony models in ComfyUI.

## Nodes

- **CyberRealistic Subject** – Build subject prompts (gender, age, ethnicity, body, hair, clothing, pose, etc.).
- **CyberRealistic Master Prompt** – Combine subjects with scene/location/lighting/camera and output positive + negative prompts.

Both appear under the **CyberRealistic Pony** category in the Add Node menu.

## If nodes don’t appear

1. **Restart ComfyUI** so it rescans custom nodes.

2. **Check the ComfyUI terminal** when it starts. Look for:
   - `Import times for custom nodes:`  
     If you see `ComfyUI-CyberRealistic-Pony` with **(IMPORT FAILED)** next to it, there is an import error; the traceback above it will show the cause.
   - If the extension is not listed at all, ComfyUI is not loading from this folder.

3. **Confirm this folder is in ComfyUI’s `custom_nodes` directory**  
   The folder that contains `main.py` and `folder_paths.py` is the ComfyUI root. This repo must be placed as:
   ```
   <ComfyUI root>/custom_nodes/ComfyUI-CyberRealistic-Pony/
   ```
   So that `custom_nodes/ComfyUI-CyberRealistic-Pony/__init__.py` and `nodes.py` exist there.

4. **In the UI**, use **Add Node** and search for **CyberRealistic** or open the **CyberRealistic Pony** category.

5. **Manager / whitelist**  
   If you use ComfyUI Manager and custom nodes are disabled by default, ensure **ComfyUI-CyberRealistic-Pony** is not disabled and is allowed (e.g. whitelisted if you use a whitelist).

---

## Summary of new SDXL Pony tags added

Tags were sourced from Pony Diffusion XL / Danbooru reference lists (Civitai articles, Danbooru tag groups) and merged into each dropdown. New or previously missing tags include:

- **Hairstyles:** `princess_head`, `centre parting bangs`, `multi-tied_hair`, `braiding_hair`, `feather_hair`, `bow-shaped_hair`, `lone_nape_hair`, `shag haircut`, `star_shaped_ahoge`, `triple_bun`, `cone_hair_bun`, `crossed_bangs`, `choppy_bangs`, `diagonal_bangs`, `dyed_bangs`, `fanged_bangs`, `long_bangs`, `parted_bangs`, `hair_intakes`, `single_hair_intake`, `asymmetrical_sidelocks`, `drill_sidelocks`, `low-tied_sidelocks`, `ooseledets`, `hair_scarf`, `one_side_up`, `two_side_up`, `low_braided_long_hair`, `low_tied_long_hair`, `mizura`, `nihongami`, `folded_ponytail`, `split_ponytail`, `star-shaped_hair`, `shiny_hair`, `glowing_hair`, `liquid_hair`, `crystal_hair`, `translucent_hair`, `polka_dot_hair`, `tentacle_hair`, `hair_vines`, `split-color_hair`, `hair_half_undone`, `ruffling_hair`, `expressive_hair`, `bouncing_hair`, `flipped_hair`, `hair_rings`, `single_hair_ring`, `quin_tails`, `front_ponytail`, `quad_braids`, and others.
- **Clothing:** `canonicals`, `bikesuit`, `wrestling_outfit`, `sailor_senshi_uniform`, `summer_uniform`, `domineering`, `chinese_style`, `traditional_clothes`, `uchikake`, `sleeveless_kimono`, `print_kimono`, `hanten_(clothes)`, `gothic`, `lolita`, `gothic_lolita`, `byzantine_fashion`, `tropical cloth`, `indian_style`, `Ao_Dai`, `ainu_clothes`, `arabian_clothes`, `egyptian_clothes`, `hawaii costume`, `furisode`, `animal_costume`, `bunny_costume`, `cat_costume`, `santa_costume`, `print_pajamas`, `hanfu`, `Taoist robe`, `halloween_costume`, `harem_outfit`, `shrug_clothing`, `tennis_uniform`, `baseball_uniform`, `blouse`, `criss-cross_halter`, `kappougi`, `sleeveless_hoodie`, `waistcoat`, `pullover_sweaters`, `ribbed_sweater`, `sweater_vest`, `backless_sweater`, `double-breasted`, `long_coat`, `winter_coat`, `hooded_coat`, `fur_coat`, `duffel_coat`, `cropped_jacket`, `track_jacket`, `hooded_track_jacket`, `camouflage_jacket`, `windbreaker`, `raincoat`, `tunic`, `cape`, `capelet`, `hagoromo`, `clothes_around_waist`, `jacket_around_waist`, `sweater_around_waist`, `loincloth`, `girdle`, `full_armor`, `japanese_armor`, `kusazuri`, `helmet`, `kabuto`, `off-shoulder_armor`, `shoulder_armor`, `muneate`, `breastplate`, `faulds`, `mini_skirt`, `skirt_suit`, `bikini_skirt`, `bubble_skirt`, `tutu`, `ballgown`, `high-waist_skirt`, `chiffon_skirt`, `lace_skirt`, `flared_skirt`, `floral_skirt`, `jumpsuit`, `hot_pants`, `suspender_shorts`, `dolphin_shorts`, `gym_shorts`, `puffy_pants`, `pumpkin_pants`, `hakama`, `hakama_pants`, `harem_pants`, `bloomers`, `buruma`, `camouflage_pants`, `capri_pants`, `chaps`, `plaid_pants`, `torn_jeans`, `rigging`, and others.
- **Locations:** `white_background`, `black_background`, `grey_background`, `blue_background`, `gradient_background`, `simple_background`, `bedroom`, `kitchen`, `office`, `gym`, `gymnasium`, `beach`, `forest`, `garden`, `street`, `mountain`, `desert`, `pool`, `rooftop`, `balcony`, `outdoors`, `indoors`, `castle`, `temple`, `church`, `dojo`, `cave`, `underwater`, `stadium`, `concert`, `bar`, `club`.
- **Lighting:** `studio_lighting`, `rim_lighting`, `backlighting`, `dramatic_lighting`, `soft_lighting`, `harsh_lighting`, `outdoor_lighting`, `indoor_lighting`, `overcast`, `night`, `day`, `sunset`, `sunrise`, `silhouette`.
- **Cameras:** `wide_shot`, `wide angle view`, `extreme close-up`, `full body shot`, `upper body`, `medium shot`, `long shot`, `bird's eye view`, `low angle`, `high angle`, `over_shoulder`.

Duplicate `Random` in **Skin types** was removed. All dropdown options now align with SDXL Pony–recognized and Danbooru-style tags where applicable.

---

## All tags (by category)

Below are all options available in the node dropdowns. Each list includes `Random` where the node supports random selection.

### Genders
`female`, `male`, `futa`, `other`, `Random`

### Ratings
`rating_safe`, `rating_questionable`, `rating_explicit`

### Ages
`18`, `20`, `25`, `30`, `35`, `40`, `45`, `50`, `60`, `MILF`, `mature`, `Random`

### Ethnicities
`Caucasian`, `Japanese`, `Korean`, `Chinese`, `African American`, `Nubian`, `Latino`, `Scandinavian`, `Italian`, `Russian`, `Middle Eastern`, `South Asian`, `Native American`, `Pacific Islander`, `Mixed Race`, `Pale-skinned`, `Dark-skinned`, `Random`

### Skin types
`Random`, `pale skin`, `fair skin`, `tan skin`, `dark skin`, `olive skin`, `freckled skin`, `textured skin with pores`, `oily skin`, `wet skin`, `sweaty skin`, `shiny skin`, `goosebumps`, `sun-damaged skin`, `perfect skin`, `soft skin`, `light skin`, `brown skin`, `black skin`, `body paint`, `tattoo`

### Hair colors
`Random`, `blonde`, `platinum_blonde`, `platinum blonde`, `dirty blonde`, `brunette`, `brown_hair`, `black`, `black_hair`, `raven black`, `red`, `red_hair`, `ginger`, `auburn`, `white`, `white_hair`, `silver`, `silver_hair`, `grey`, `grey_hair`, `blue_hair`, `green_hair`, `pink_hair`, `pastel pink`, `neon blue`, `purple`, `azure_hair`, `aqua_hair`, `ruby_hair`, `rainbow_hair`, `rainbow`, `multicolored_hair`, `two-tone_hair`, `two-tone`, `ombre`, `gradient_hair`, `streaked_hair`, `dyed_hair`

### Eye colors
`Random`, `blue`, `blue_eyes`, `ice blue`, `green`, `green_eyes`, `emerald`, `brown`, `brown_eyes`, `hazel`, `grey`, `grey_eyes`, `amber`, `red`, `red_eyes`, `purple`, `purple_eyes`, `heterochromia`, `glowing eyes`, `closed eyes`, `half-closed eyes`, `aqua_eyes`, `gold_eyes`, `yellow_eyes`, `pink_eyes`, `black_eyes`

### Hairstyles
`Random`, `straight_hair`, `curly_hair`, `wavy_hair`, `long straight`, `long wavy`, `messy_hair`, `messy bun`, `bob cut`, `inverted_bob`, `princess_cut`, `princess_head`, `bowl_cut`, `hime cut`, `hime_cut`, `hair_flaps`, `bangs`, `air_bangs`, `blunt_bangs`, `side_blunt_bangs`, `centre parting bangs`, `swept bangs`, `swept_bangs`, `asymmetric bangs`, `braided_bangs`, `ponytail`, `twintails`, `twin tails`, `short_ponytail`, `side_ponytail`, `high_ponytail`, `low_twintails`, `short_twintails`, `uneven_twintails`, `tri_tails`, `quad_tails`, `quin_tails`, `tied_hair`, `low_tied_hair`, `multi-tied_hair`, `braid`, `french_braid`, `braiding_hair`, `braided ponytail`, `twin_braids`, `short_braid`, `long_braid`, `braided_bun`, `braided_ponytail`, `crown_braid`, `multiple_braids`, `side_braid`, `hair_bun`, `double_bun`, `single_hair_bun`, `ballet_hair_bun`, `doughnut_hair_bun`, `heart_hair_bun`, `triple_bun`, `cone_hair_bun`, `half_updo`, `half_up_braid`, `half_up_half_down_braid`, `pointy_hair`, `feather_hair`, `bow-shaped_hair`, `lone_nape_hair`, `shag haircut`, `ahoge`, `heart_shaped_ahoge`, `star_shaped_ahoge`, `antenna_hair`, `sideburns`, `long_sideburns`, `sidelocks`, `hair_over_one_eye`, `hair_over_eyes`, `shaved side`, `undercut`, `afro`, `huge_afro`, `spiked_hair`, `dreadlocks`, `cornrows`, `boxing_braids`, `mullet`, `pompadour`, `quiff`, `messy quiff`, `short curly`, `ringlets`, `crew cut`, `buzz cut`, `flattop`, `fade`, `man bun`, `bald`, `hair_slicked_back`, `slicked back`, `side part`, `hair_pulled_back`, `hair_comb_over`, `very_short_hair`, `very_long_hair`, `absurdly_long_hair`, `wolf cut`, `wolf_cut`, `mohawk`, `chonmage`, `okappa`, `front_braid`, `front_ponytail`, `low_twin_braids`, `tri_braids`, `quad_braids`, `japari_bun`, `arched_bangs`, `asymmetrical_bangs`, `bangs_pinned_back`, `crossed_bangs`, `choppy_bangs`, `diagonal_bangs`, `dyed_bangs`, `fanged_bangs`, `long_bangs`, `parted_bangs`, `curtained_hair`, `wispy_bangs`, `short_bangs`, `hair_between_eyes`, `sidelocks_tied_back`, `single_sidelock`, `widow's peak`, `huge_ahoge`, `hair_intakes`, `single_hair_intake`, `asymmetrical_sidelocks`, `drill_sidelocks`, `low-tied_sidelocks`, `drill_hair`, `twin_drills`, `tri_drills`, `beehive_hairdo`, `flower_shaped_hair`, `twisted_hair`, `ooseledets`, `hair_scarf`, `one_side_up`, `two_side_up`, `low_braided_long_hair`, `low_tied_long_hair`, `mizura`, `nihongami`, `folded_ponytail`, `split_ponytail`, `star-shaped_hair`, `shiny_hair`, `glowing_hair`, `liquid_hair`, `crystal_hair`, `translucent_hair`, `polka_dot_hair`, `tentacle_hair`, `hair_vines`, `split-color_hair`, `hair_half_undone`, `ruffling_hair`, `expressive_hair`, `bouncing_hair`, `flipped_hair`, `hair_rings`, `single_hair_ring`, `long flowing`, `updo`, `short textured`

### Clothing
`Random`, `nude`, `lingerie`, `lace underwear`, `bikini`, `micro bikini`, `one-piece swimsuit`, `shell_bikini`, `frilled_swimsuit`, `front_zipper_swimsuit`, `bikesuit`, `wrestling_outfit`, `evening_gown`, `evening gown`, `cocktail_dress`, `cocktail dress`, `gown`, `wedding_dress`, `canonicals`, `sundress`, `summer dress`, `sleeveless_dress`, `strapless_dress`, `backless_dress`, `halter_dress`, `sailor_dress`, `pinafore_dress`, `frilled_dress`, `sweater_dress`, `pleated_dress`, `pencil_dress`, `cheongsam`, `china_dress`, `off-shoulder_dress`, `armored_dress`, `fur-trimmed_dress`, `lace-trimmed_dress`, `collared_dress`, `layered_dress`, `multicolored_dress`, `striped_dress`, `checkered_skirt`, `polka_dot_dress`, `plaid_dress`, `print_dress`, `ribbed_dress`, `short_jumpsuit`, `maid`, `miko`, `school_uniform`, `sailor`, `serafuku`, `sailor_senshi_uniform`, `summer_uniform`, `naval_uniform`, `military_uniform`, `business_suit`, `business suit`, `nurse`, `chef_uniform`, `labcoat`, `cheerleader`, `band_uniform`, `space_suit`, `leotard`, `domineering`, `hanbok`, `japanese_clothes`, `chinese_style`, `traditional_clothes`, `uchikake`, `sleeveless_kimono`, `print_kimono`, `hanten_(clothes)`, `korean_clothes`, `gothic`, `lolita`, `gothic_lolita`, `byzantine_fashion`, `tropical cloth`, `indian_style`, `Ao_Dai`, `ainu_clothes`, `arabian_clothes`, `egyptian_clothes`, `hawaii costume`, `furisode`, `animal_costume`, `bunny_costume`, `cat_costume`, `santa_costume`, `hoodie`, `pajamas`, `nightgown`, `sleepwear`, `print_pajamas`, `yukata`, `hanfu`, `Taoist robe`, `robe`, `cloak`, `hooded_cloak`, `winter_clothes`, `down jacket`, `halloween_costume`, `loungewear`, `santa`, `harem_outfit`, `shrug_clothing`, `gym_uniform`, `athletic_leotard`, `volleyball_uniform`, `tennis_uniform`, `baseball_uniform`, `letterman_jacket`, `biker_clothes`, `t-shirt`, `blouse`, `off-shoulder_shirt`, `collared_shirt`, `collared shirt`, `dress_shirt`, `sailor_shirt`, `cropped_shirt`, `criss-cross_halter`, `frilled_shirt`, `sweatshirt`, `hawaiian_shirt`, `kappougi`, `polo_shirt`, `polo shirt`, `print_shirt`, `sleeveless_hoodie`, `sleeveless_shirt`, `striped_shirt`, `tank_top`, `tank top`, `vest`, `waistcoat`, `cardigan`, `sweater`, `virgin killer sweater`, `hooded_sweater`, `striped_sweater`, `pullover_sweaters`, `ribbed_sweater`, `sweater_vest`, `backless_sweater`, `blazer`, `overcoat`, `double-breasted`, `long_coat`, `winter_coat`, `hooded_coat`, `fur_coat`, `fur-trimmed_coat`, `duffel_coat`, `parka`, `cropped_jacket`, `track_jacket`, `hooded_track_jacket`, `military_jacket`, `camouflage_jacket`, `leather_jacket`, `leather jacket`, `trench_coat`, `windbreaker`, `raincoat`, `tunic`, `cape`, `capelet`, `hagoromo`, `waist_apron`, `maid_apron`, `clothes_around_waist`, `jacket_around_waist`, `sweater_around_waist`, `loincloth`, `corset`, `bustier`, `girdle`, `armor`, `bikini_armor`, `full_armor`, `plate_armor`, `japanese_armor`, `kusazuri`, `power_armor`, `helmet`, `kabuto`, `off-shoulder_armor`, `shoulder_armor`, `muneate`, `breastplate`, `faulds`, `skirt`, `miniskirt`, `mini_skirt`, `skirt_suit`, `bikini_skirt`, `pleated_skirt`, `pencil_skirt`, `bubble_skirt`, `tutu`, `ballgown`, `denim_skirt`, `suspender_skirt`, `long_skirt`, `high-waist_skirt`, `chiffon_skirt`, `lace_skirt`, `layered_skirt`, `print_skirt`, `flared_skirt`, `floral_skirt`, `jumpsuit`, `hot_pants`, `striped_shorts`, `suspender_shorts`, `denim_shorts`, `puffy_shorts`, `dolphin_shorts`, `tight pants`, `yoga pants`, `track_pants`, `bike_shorts`, `gym_shorts`, `pants`, `puffy_pants`, `pumpkin_pants`, `hakama`, `hakama_pants`, `harem_pants`, `bloomers`, `buruma`, `jeans`, `cargo_pants`, `camouflage_pants`, `capri_pants`, `chaps`, `plaid_pants`, `striped_pants`, `torn_jeans`, `boxers`, `briefs`, `swim trunks`, `tuxedo`, `tailored suit`, `fishnets`, `thighhighs`, `latex bodysuit`, `towel`, `apron`, `harness`, `rigging`, `lab coat`, `mechanic jumpsuit`, `biker vest`, `streetwear`, `casual`, `cyberpunk techwear`

### Body types
`Random`, `slim body`, `curvy body`, `voluptuous body`, `hourglass figure`, `hourglass`, `athletic body`, `fit body`, `petite body`, `tall body`, `plus size body`, `thick thighs`, `wide hips`, `soft body`, `pregnant`, `muscular body`, `lean body`, `broad shoulders`, `muscular`, `dad bod`, `slim fit`, `bodybuilder`, `average build`, `hairy chest`, `abs`, `bear`, `flat_chest`, `large_breasts`, `huge_breasts`, `long neck`, `navel`, `cleavage`, `ass`, `medium build`, `skinny`, `stocky`, `obese`, `toned`

### Poses
`Random`, `standing`, `standing elegantly`, `sitting`, `sitting on chair`, `kneeling`, `all fours`, `lying on back`, `lying on stomach`, `walking`, `looking back`, `looking at viewer`, `hands on hips`, `peace sign`, `selfie angle`, `twirling hair`, `leaning against wall`, `legs spread`, `bent over`, `squatting`, `stretching`, `presenting`, `lifting skirt`, `spread legs`, `standing confidently`, `sitting manspreading`, `arms crossed`, `adjusting tie`, `hands in pockets`, `hand on hip`, `fighting stance`, `flexing muscles`, `dynamic action`, `floating`, `dancing`, `running`, `jumping`, `yawning`, `leg crossed`, `arms up`, `on back`, `on stomach`, `cowboy shot`, `from below`, `from above`, `profile`, `back to viewer`, `reclining`, `standing on one leg`

### Breast sizes
`Random`, `None`, `flat chest`, `small breasts`, `medium breasts`, `large breasts`, `huge breasts`, `gigantic breasts`, `massive breasts`

### Breast shapes
`Random`, `None`, `natural breasts`, `perky breasts`, `saggy breasts`, `asymmetrical breasts`, `perfect breasts`, `heavy breasts`

### Locations
`Random`, `simple white background`, `white_background`, `simple black background`, `black_background`, `grey background`, `grey_background`, `blue_background`, `gradient_background`, `simple_background`, `photography studio`, `bustling city street`, `cyberpunk city at night`, `luxury penthouse`, `cozy bedroom`, `bedroom`, `messy bedroom`, `modern kitchen`, `kitchen`, `bathroom`, `shower stall`, `locker room`, `neon-lit club`, `bar counter`, `library`, `cafe terrace`, `classroom`, `office cubicle`, `office`, `hospital room`, `garage`, `dungeon`, `gym`, `gymnasium`, `sci-fi spaceship interior`, `space station corridor`, `beach`, `beach sunset`, `dense forest`, `forest`, `flower garden`, `garden`, `abandoned warehouse`, `rainy street`, `street`, `snowy mountain`, `mountain`, `desert dunes`, `desert`, `tropical jungle`, `meadow with flowers`, `onsen`, `in a pool`, `pool`, `rooftop`, `rooftop at night`, `balcony`, `autumn park`, `cherry blossom grove`, `love hotel`, `tatami room`, `public train`, `outdoors`, `indoors`, `castle`, `temple`, `church`, `dojo`, `cave`, `underwater`, `stadium`, `concert`, `bar`, `club`

### Lighting
`Random`, `natural sunlight`, `golden hour`, `soft overcast`, `cinematic lighting`, `studio softbox`, `studio_lighting`, `hard rim lighting`, `rim_lighting`, `backlighting`, `neon lights`, `volumetric fog`, `dark moody lighting`, `dramatic_lighting`, `moonlight`, `bioluminescent glow`, `camera flash`, `dimly lit`, `candlelight`, `god rays`, `lens flare`, `soft_lighting`, `harsh_lighting`, `outdoor_lighting`, `indoor_lighting`, `overcast`, `night`, `day`, `sunset`, `sunrise`, `silhouette`

### Cameras
`Random`, `85mm portrait lens`, `35mm street lens`, `24mm wide angle`, `50mm standard lens`, `200mm telephoto`, `macro lens`, `fisheye lens`, `wide_shot`, `wide angle view`, `CCTV footage`, `Polaroid style`, `GoPro view`, `drone shot`, `from below`, `from above`, `dutch angle`, `close-up`, `extreme close-up`, `cowboy shot`, `full body`, `full body shot`, `upper body`, `medium shot`, `long shot`, `bird's eye view`, `low angle`, `high angle`, `over_shoulder`, `pov`, `looking at viewer`

### Sex acts (optional, NSFW)
`None`, `Random`, `sex`, `vaginal sex`, `anal sex`, `oral sex`, `fellatio`, `cunnilingus`, `sixty-nine`, `fingering`, `handjob`, `paizuri`, `titfuck`, `rimming`, `footjob`, `thigh job`, `frottage`, `tribadism`, `deepthroat`, `face fucking`, `irrumatio`, `double penetration`, `gangbang`, `bukkake`, `creampie`, `facial`, `internal ejaculation`, `masturbation`, `spitroast`, `group sex`

### Sex positions (optional, NSFW)
`None`, `Random`, `missionary`, `doggy style`, `cowgirl position`, `reverse cowgirl`, `mating press`, `standing sex`, `spooning sex`, `piledriver`, `amazon position`, `carried sex`, `against wall`, `on desk`, `suspended`, `facesitting`, `prone bone`, `legs over shoulders`, `lotus position`, `bridge position`, `bent over`

### NSFW modifiers (optional)
`nude`, `naked`, `topless`, `bottomless`, `nipples`, `areolae`, `pussy juice`, `sweat`, `tears`, `blush`, `ahegao`, `rolling eyes`, `tongue out`, `drooling`, `hard nipples`, `detailed genitals`, `uncensored`, `cum on body`, `cum on face`, `messy hair`, `heavy breathing`
