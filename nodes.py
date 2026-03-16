import random

# --- DATA CONSTANTS (Ported from the Web App) ---

GENDERS = ["female", "male", "futa", "other", "Random"]
RATINGS = ["rating_safe", "rating_questionable", "rating_explicit"]

SCORE_SCHEMES = [
    "default high",          # score_9, score_8_up, score_7_up, score_6_up
    "score_9 only",          # score_9
    "score_7_plus",          # score_9, score_8_up, score_7_up
]

SOURCE_TAGS = [
    "None",
    "source_photography",
    "source_pony",
    "source_furry",
    "source_anime",
    "source_cartoon",
]

STYLE_PRESETS = [
    "None",
    "photorealistic",
    "anime_leaning",
    "sketch",
    "studio_glamour",
]

AGES = ["18", "20", "25", "30", "35", "40", "45", "50", "60", "MILF", "mature", "Random"]

ETHNICITIES = [
    "Caucasian", "Japanese", "Korean", "Chinese", "African American", "Nubian",
    "Latino", "Scandinavian", "Italian", "Russian", "Middle Eastern", "South Asian",
    "Native American", "Pacific Islander", "Mixed Race", "Pale-skinned", "Dark-skinned", "Random"
]

SKIN_TYPES = [
    "Random",
    "pale skin", "fair skin", "tan skin", "dark skin", "olive skin",
    "freckled skin", "textured skin with pores", "oily skin", "wet skin", "sweaty skin",
    "shiny skin", "goosebumps", "sun-damaged skin", "perfect skin", "soft skin",
    "light skin", "brown skin", "black skin", "body paint", "tattoo"
]

HAIR_COLORS = [
    "Random",
    "blonde", "platinum_blonde", "platinum blonde", "dirty blonde", "brunette", "brown_hair",
    "black", "black_hair", "raven black", "red", "red_hair", "ginger", "auburn",
    "white", "white_hair", "silver", "silver_hair", "grey", "grey_hair",
    "blue_hair", "green_hair", "pink_hair", "pastel pink", "neon blue", "purple",
    "azure_hair", "aqua_hair", "ruby_hair", "rainbow_hair", "rainbow",
    "multicolored_hair", "two-tone_hair", "two-tone", "ombre", "gradient_hair",
    "streaked_hair", "dyed_hair"
]

EYE_COLORS = [
    "Random",
    "blue", "blue_eyes", "ice blue", "green", "green_eyes", "emerald", "brown", "brown_eyes",
    "hazel", "grey", "grey_eyes", "amber", "red", "red_eyes", "purple", "purple_eyes",
    "heterochromia", "glowing eyes", "closed eyes", "half-closed eyes",
    "aqua_eyes", "gold_eyes", "yellow_eyes", "pink_eyes", "black_eyes"
]

# Pony/Danbooru tag lists (male + female) for ComfyUI dropdowns — SDXL Pony recognized
ALL_HAIRSTYLES = [
    "Random",
    "straight_hair", "curly_hair", "wavy_hair", "long straight", "long wavy",
    "messy_hair", "messy bun", "bob cut", "inverted_bob", "princess_cut", "princess_head", "bowl_cut",
    "hime cut", "hime_cut", "hair_flaps", "bangs", "air_bangs", "blunt_bangs", "side_blunt_bangs",
    "centre parting bangs", "swept bangs", "swept_bangs", "asymmetric bangs", "braided_bangs",
    "ponytail", "twintails", "twin tails", "short_ponytail", "side_ponytail", "high_ponytail",
    "low_twintails", "short_twintails", "uneven_twintails", "tri_tails", "quad_tails", "quin_tails",
    "tied_hair", "low_tied_hair", "multi-tied_hair", "braid", "french_braid", "braiding_hair",
    "braided ponytail", "twin_braids", "short_braid", "long_braid", "braided_bun", "braided_ponytail",
    "crown_braid", "multiple_braids", "side_braid", "hair_bun", "double_bun", "single_hair_bun",
    "ballet_hair_bun", "doughnut_hair_bun", "heart_hair_bun", "triple_bun", "cone_hair_bun",
    "half_updo", "half_up_braid", "half_up_half_down_braid", "pointy_hair", "feather_hair",
    "bow-shaped_hair", "lone_nape_hair", "shag haircut", "ahoge", "heart_shaped_ahoge",
    "star_shaped_ahoge", "antenna_hair", "sideburns", "long_sideburns", "sidelocks",
    "hair_over_one_eye", "hair_over_eyes", "shaved side", "undercut", "afro", "huge_afro",
    "spiked_hair", "dreadlocks", "cornrows", "boxing_braids", "mullet", "pompadour", "quiff",
    "messy quiff", "short curly", "ringlets", "crew cut", "buzz cut", "flattop", "fade",
    "man bun", "bald", "hair_slicked_back", "slicked back", "side part", "hair_pulled_back",
    "hair_comb_over", "very_short_hair", "very_long_hair", "absurdly_long_hair", "wolf cut",
    "wolf_cut", "mohawk", "chonmage", "okappa", "front_braid", "front_ponytail", "low_twin_braids",
    "tri_braids", "quad_braids", "japari_bun", "arched_bangs", "asymmetrical_bangs",
    "bangs_pinned_back", "crossed_bangs", "choppy_bangs", "diagonal_bangs", "dyed_bangs",
    "fanged_bangs", "long_bangs", "parted_bangs", "curtained_hair", "wispy_bangs", "short_bangs",
    "hair_between_eyes", "sidelocks_tied_back", "single_sidelock", "widow's peak", "huge_ahoge",
    "hair_intakes", "single_hair_intake", "asymmetrical_sidelocks", "drill_sidelocks",
    "low-tied_sidelocks", "drill_hair", "twin_drills", "tri_drills", "beehive_hairdo",
    "flower_shaped_hair", "twisted_hair", "ooseledets", "hair_scarf", "one_side_up",
    "two_side_up", "low_braided_long_hair", "low_tied_long_hair", "mizura", "nihongami",
    "folded_ponytail", "split_ponytail", "star-shaped_hair", "shiny_hair", "glowing_hair",
    "liquid_hair", "crystal_hair", "translucent_hair", "polka_dot_hair", "tentacle_hair",
    "hair_vines", "split-color_hair", "hair_half_undone", "ruffling_hair", "expressive_hair",
    "bouncing_hair", "flipped_hair", "hair_rings", "single_hair_ring", "long flowing", "updo",
    "short textured"
]

# Simple gendered views over ALL_HAIRSTYLES.
FEMALE_HAIRSTYLES = [
    "Random",
    "long straight", "long wavy", "messy_hair", "messy bun", "bob cut", "inverted_bob",
    "princess_cut", "princess_head", "hime cut", "hime_cut",
    "ponytail", "twintails", "twin tails", "short_ponytail", "side_ponytail", "high_ponytail",
    "low_twintails", "short_twintails", "uneven_twintails",
    "braid", "french_braid", "braiding_hair", "braided ponytail", "twin_braids",
    "long_braid", "braided_bun", "braided_ponytail", "crown_braid", "multiple_braids",
    "side_braid", "hair_bun", "double_bun", "single_hair_bun", "ballet_hair_bun",
    "doughnut_hair_bun", "heart_hair_bun", "triple_bun", "cone_hair_bun",
    "half_updo", "half_up_braid", "half_up_half_down_braid",
    "arched_bangs", "asymmetrical_bangs", "bangs_pinned_back", "choppy_bangs",
    "curtained_hair", "wispy_bangs", "long_bangs", "short_bangs",
    "hair_between_eyes", "sidelocks_tied_back", "single_sidelock",
    "long flowing", "updo", "short textured", "shag haircut",
]

MALE_HAIRSTYLES = [
    "Random",
    "short textured", "short curly", "crew cut", "buzz cut", "flattop", "fade",
    "mullet", "pompadour", "quiff", "messy quiff",
    "man bun", "bald", "hair_slicked_back", "slicked back", "side part",
    "undercut", "shaved side", "spiked_hair",
]

FULL_OUTFITS = [
    "Random",
    "nude", "lingerie", "lace underwear", "bikini", "micro bikini", "one-piece swimsuit",
    "shell_bikini", "frilled_swimsuit", "front_zipper_swimsuit", "bikesuit", "wrestling_outfit",
    "evening_gown", "evening gown", "cocktail_dress", "cocktail dress", "gown", "wedding_dress",
    "canonicals", "sundress", "summer dress", "sleeveless_dress", "strapless_dress", "backless_dress",
    "halter_dress", "sailor_dress", "pinafore_dress", "frilled_dress", "sweater_dress",
    "pleated_dress", "pencil_dress", "cheongsam", "china_dress", "off-shoulder_dress",
    "armored_dress", "fur-trimmed_dress", "lace-trimmed_dress", "collared_dress", "layered_dress",
    "multicolored_dress", "striped_dress", "polka_dot_dress", "plaid_dress",
    "print_dress", "ribbed_dress", "short_jumpsuit", "maid", "miko", "school_uniform", "sailor",
    "serafuku", "sailor_senshi_uniform", "summer_uniform", "naval_uniform", "military_uniform",
    "business_suit", "business suit", "nurse", "chef_uniform", "labcoat", "cheerleader",
    "band_uniform", "space_suit", "leotard", "hanbok", "japanese_clothes",
    "chinese_style", "traditional_clothes", "uchikake", "sleeveless_kimono", "print_kimono",
    "hanten_(clothes)", "korean_clothes", "gothic", "lolita", "gothic_lolita", "byzantine_fashion",
    "tropical cloth", "indian_style", "Ao_Dai", "ainu_clothes", "arabian_clothes", "egyptian_clothes",
    "hawaii costume", "furisode", "animal_costume", "bunny_costume", "cat_costume", "santa_costume",
    "yukata", "hanfu", "Taoist robe", "robe", "cloak", "hooded_cloak", "winter_clothes",
    "down jacket", "halloween_costume", "loungewear", "harem_outfit", "gym_uniform",
    "athletic_leotard", "volleyball_uniform", "tennis_uniform", "baseball_uniform",
    "letterman_jacket", "biker_clothes", "tuxedo", "tailored suit", "latex bodysuit",
    "mechanic jumpsuit", "streetwear", "casual", "cyberpunk techwear"
]

TOP_CLOTHING = [
    "Random", "None",
    "t-shirt", "blouse", "off-shoulder_shirt", "collared_shirt", "collared shirt", "dress_shirt",
    "sailor_shirt", "cropped_shirt", "criss-cross_halter", "frilled_shirt", "sweatshirt",
    "hawaiian_shirt", "kappougi", "polo_shirt", "polo shirt", "print_shirt", "sleeveless_hoodie",
    "sleeveless_shirt", "striped_shirt", "tank_top", "tank top", "vest", "waistcoat", "cardigan",
    "sweater", "virgin killer sweater", "hooded_sweater", "striped_sweater", "pullover_sweaters",
    "ribbed_sweater", "sweater_vest", "backless_sweater", "blazer", "overcoat", "double-breasted",
    "long_coat", "winter_coat", "hooded_coat", "fur_coat", "fur-trimmed_coat", "duffel_coat",
    "parka", "cropped_jacket", "track_jacket", "hooded_track_jacket", "military_jacket",
    "camouflage_jacket", "leather_jacket", "leather jacket", "trench_coat", "windbreaker",
    "raincoat", "tunic", "cape", "capelet", "hagoromo", "lab coat", "biker vest",
    "crop_top", "sports_bra", "tube_top", "halter_top", "bustier", "corset", "hoodie",
    "zipper_jacket", "denim_jacket", "puffer_jacket", "sleeveless_turtleneck", "turtleneck_sweater",
    "off_shoulder_sweater", "graphic_tshirt", "logo_tshirt",
    # Additional common Danbooru-style tops
    "open_shirt", "unbuttoned_shirt", "see-through_shirt", "wet_shirt",
    "white_shirt", "black_shirt", "striped_t-shirt", "graphic_t-shirt",
    "off_shoulder_top", "cropped_hoodie", "hood_down", "hood_up",
    "sleeveless_sweater", "ribbed_tank_top", "sports_jacket", "jersey"
]

FEMALE_TOP_CLOTHING = [
    "Random", "None",
    "blouse", "off-shoulder_shirt", "cropped_shirt", "criss-cross_halter",
    "frilled_shirt", "virgin killer sweater", "backless_sweater",
    "crop_top", "sports_bra", "tube_top", "halter_top", "bustier", "corset",
    "off_shoulder_sweater", "sleeveless_sweater", "ribbed_tank_top",
]

MALE_TOP_CLOTHING = [
    "Random", "None",
    "t-shirt", "dress_shirt", "collared_shirt", "collared shirt", "sailor_shirt",
    "polo_shirt", "polo shirt", "sweatshirt", "hawaiian_shirt",
    "track_jacket", "hooded_track_jacket", "military_jacket",
    "letterman_jacket", "sports_jacket", "jersey",
]

BOTTOM_CLOTHING = [
    "Random", "None",
    "skirt", "miniskirt", "mini_skirt", "skirt_suit", "bikini_skirt",
    "pleated_skirt", "pencil_skirt", "bubble_skirt", "tutu", "ballgown", "denim_skirt",
    "suspender_skirt", "long_skirt", "high-waist_skirt", "chiffon_skirt", "lace_skirt",
    "layered_skirt", "print_skirt", "flared_skirt", "floral_skirt", "jumpsuit", "hot_pants",
    "striped_shorts", "suspender_shorts", "denim_shorts", "puffy_shorts", "dolphin_shorts",
    "tight pants", "yoga pants", "track_pants", "bike_shorts", "gym_shorts", "pants",
    "puffy_pants", "pumpkin_pants", "hakama", "hakama_pants", "harem_pants", "bloomers", "buruma",
    "jeans", "cargo_pants", "camouflage_pants", "capri_pants", "chaps", "plaid_pants",
    "striped_pants", "torn_jeans", "boxers", "briefs", "swim trunks", "loincloth",
    "leggings", "fishnet_pantyhose", "ripped_jeans", "short_shorts", "yoga_shorts",
    "denim_cutoffs", "thigh_straps", "garter_straps",
    # Additional Danbooru-style bottoms and legwear
    "booty_shorts", "low_rise_shorts", "high-waist_shorts", "tight_shorts",
    "striped_thighhighs", "vertical-striped_thighhighs", "polka_dot_thighhighs",
    "ripped_leggings", "sheer_pantyhose", "patterned_pantyhose",
    "striped_panties", "lacy_panties", "thong", "g-string"
]

HEADWEAR = [
    "Random", "None",
    "helmet", "kabuto", "hat", "beret", "baseball cap", "sun hat", "headband",
    "hairband", "tiara", "crown", "veil", "hood", "hood_up", "headphones",
    "beanie", "newsboy_cap", "cowboy_hat", "straw_hat", "witch_hat", "wizard_hat",
    "ribbon_in_hair", "hair_ribbon",
    # Additional common head items
    "hair_ornament", "hair_flower", "flower_crown", "laurel_wreath",
    "nurse_cap", "maid_headdress", "military_hat", "police_hat",
    "beret_with_badge", "animal_ears_hat", "cat_ears_hood", "bunny_ears_hood"
]

FOOTWEAR = [
    "Random", "None",
    "barefoot", "sandals", "flip_flops", "sneakers", "running shoes", "boots", "thigh_boots",
    "knee_high_boots", "ankle_boots", "loafers", "high_heels", "stilettos", "platform_shoes",
    "mary_janes", "combat_boots", "lace_up_boots", "thighhigh_boots", "wedge_heels",
    # Additional footwear / legwear tags
    "geta", "zori", "school_shoes", "heels", "platform_boots",
    "open_toe_sandals", "ankle_strap_heels", "knee_socks", "thighhigh_socks",
    "mismatched_socks", "striped_socks"
]

ACCESSORIES = [
    "Random", "None",
    "fishnets", "thighhighs", "stockings", "pantyhose", "garter_belt",
    "arm warmers", "fingerless gloves", "gloves", "scarf", "necktie", "bowtie",
    "choker", "necklace", "bracelet", "ring", "earrings", "sunglasses",
    "goggles", "backpack", "messenger bag", "belt", "harness", "rigging",
    "waist_apron", "maid_apron", "clothes_around_waist", "jacket_around_waist",
    "sweater_around_waist", "towel", "apron",
    "suspenders", "necklace_choker", "locket", "pierced_ears", "nose_ring",
    "belly_chain", "anklet", "armlet", "wristband", "watch", "hairclip",
    "hair_flower", "cat_ears_headband", "bunny_ears_headband",
    # Additional accessories and fetish-leaning details
    "hair_ornament", "hair_ribbon", "neck_ribbon", "leg_garter",
    "collar", "leash", "handcuffs", "wrist_cuffs", "ankle_cuffs",
    "blindfold", "ball_gag", "ring_gag", "rope_bondage", "shibari",
    "bandage", "eyepatch", "monocle", "mask", "face_mask",
    "cross_necklace", "rosary", "ear_cuffs", "toe_ring"
]

ALL_BODY_TYPES = [
    "Random",
    "slim body", "curvy body", "voluptuous body", "hourglass figure", "hourglass",
    "athletic body", "fit body", "petite body", "tall body", "plus size body",
    "thick thighs", "wide hips", "soft body", "pregnant", "wide hips",
    "muscular body", "lean body", "broad shoulders", "muscular",
    "dad bod", "slim fit", "bodybuilder", "average build",
    "hairy chest", "abs", "bear", "flat_chest", "large_breasts", "huge_breasts",
    "long neck", "broad shoulders", "navel", "cleavage", "ass",
    "medium build", "skinny", "stocky", "obese", "toned",
    "pear-shaped_body", "apple-shaped_body", "hourglass_figure", "thicc",
    "lean_muscular", "soft_thick", "petite_curvy",
    # Additional nuanced body descriptors
    "muscular_female", "muscular_male", "slim_thick", "curvy_thick",
    "flat_figured", "plump", "chubby", "soft_body", "skinny_fat",
    "hourglass_waist", "broad_hips", "narrow_waist", "pear_shaped",
    "apple_shaped", "athletic_female", "athletic_male"
]

FEMALE_BODY_TYPES = [
    "Random",
    "slim body", "curvy body", "voluptuous body", "hourglass figure", "hourglass",
    "athletic_female", "petite body", "plus size body",
    "thick thighs", "wide hips", "soft body", "pregnant",
    "medium build", "skinny", "toned", "thicc", "soft_thick", "petite_curvy",
    "curvy_thick", "hourglass_waist", "broad_hips", "narrow_waist",
]

MALE_BODY_TYPES = [
    "Random",
    "athletic_male", "muscular body", "lean body", "broad shoulders", "muscular",
    "dad bod", "slim fit", "bodybuilder", "average build",
    "hairy chest", "abs", "bear",
    "medium build", "skinny", "stocky", "obese", "toned",
]

ALL_POSES = [
    "Random",
    "standing", "standing elegantly", "sitting", "sitting on chair", "kneeling", "all fours",
    "lying on back", "lying on stomach", "walking", "looking back", "looking at viewer",
    "hands on hips", "peace sign", "selfie angle", "twirling hair",
    "leaning against wall", "legs spread", "bent over", "squatting", "stretching",
    "presenting", "lifting skirt", "spread legs",
    "standing confidently", "sitting manspreading", "arms crossed",
    "adjusting tie", "hands in pockets", "hand on hip",
    "fighting stance", "flexing muscles", "dynamic action", "floating",
    "dancing", "running", "jumping", "yawning", "leg crossed", "arms up",
    "on back", "on stomach", "cowboy shot", "from below", "from above",
    "profile", "back to viewer", "reclining", "standing on one leg",
    "sitting_crosslegged", "knees_together_feet_apart", "on_tiptoes",
    "arched_back", "hip_thrust", "lying_on_side", "pinup_pose"
]

BREAST_SIZES = [
    "Random", "None", "flat chest", "small breasts", "medium breasts", "large breasts",
    "huge breasts", "gigantic breasts", "massive breasts",
    # Alternate/common boob size phrasings
    "tiny breasts", "petite breasts", "big breasts", "enormous breasts", "colossal breasts"
]

BREAST_SHAPES = [
    "Random", "None", "natural breasts", "perky breasts", "saggy breasts", "asymmetrical breasts",
    "perfect breasts", "heavy breasts",
    # Additional shape/behavior descriptors
    "round breasts", "teardrop breasts", "firm breasts", "bouncy breasts",
    "compressed_breasts", "squeezed_breasts", "hanging_breasts"
]

LEG_FEATURES = [
    "Random", "None",
    "long legs", "thick thighs", "slim legs", "muscular legs", "crossed legs",
    "legs together", "legs apart", "one leg up", "kneeling", "squatting",
    "thigh_gap", "spread_legs", "pressed_thighs", "stocking_clad_legs",
    # Additional leg focus tags
    "bare_legs", "closed_legs", "bent_legs", "leg_lift", "legs_over_edge",
    "knees_up", "leg_wrap", "leg_lock", "one_leg_on_table"
]

BUTT_FEATURES = [
    "Random", "None",
    "bubble butt", "big ass", "round butt", "tight butt", "wide hips", "plump butt",
    "perky_butt", "thong_visible", "ass_focus",
    # Additional butt / hip focus tags
    "ass_cheeks", "ass_visible_through_clothes", "panties_around_one_leg",
    "panties_around_thigh", "panties_half_off", "butt_up", "hips_out",
    "booty_focus", "ass_grab"
]

FACE_SHAPES = [
    "Random", "None",
    "round face", "oval face", "heart-shaped face", "square jaw", "sharp jawline",
    "soft features"
]

EXPRESSIONS = [
    "Random", "None",
    "neutral expression", "gentle smile", "big smile", "smirk", "serious",
    "blushing", "shy", "seductive smile", "open mouth", "tongue out",
    "ahegao", "half-lidded eyes", "closed eyes", "crying", "pouting",
    "wink", "smug", "embarrassed", "teary_eyes", "biting_lip",
    "bedroom_eyes", "sleepy", "surprised", "angry",
    # Additional Danbooru-style facial expressions
    "orgasm_face", "ecstatic", "grin", "evil_grin", "nervous_smile",
    "flustered", "scared", "terrified", "bored", "disgusted",
    "sweatdrop", "determined", "focused", "daydreaming"
]

HAIR_LENGTHS = [
    "Random", "None",
    "very_short_hair", "short hair", "medium hair", "long hair",
    "very_long_hair", "absurdly_long_hair"
]

LOCATIONS = [
    "Random",
    "simple white background", "white_background", "simple black background", "black_background",
    "grey background", "grey_background", "blue_background", "gradient_background", "simple_background",
    "photography studio", "bustling city street", "cyberpunk city at night", "luxury penthouse",
    "cozy bedroom", "bedroom", "messy bedroom", "modern kitchen", "kitchen", "bathroom", "shower stall",
    "locker room", "neon-lit club", "bar counter", "library", "cafe terrace", "classroom",
    "office cubicle", "office", "hospital room", "garage", "dungeon", "gym", "gymnasium",
    "sci-fi spaceship interior", "space station corridor", "beach", "beach sunset", "dense forest",
    "forest", "flower garden", "garden", "abandoned warehouse", "rainy street", "street",
    "snowy mountain", "mountain", "desert dunes", "desert", "tropical jungle", "meadow with flowers",
    "onsen", "in a pool", "pool", "rooftop", "rooftop at night", "balcony", "autumn park",
    "cherry blossom grove", "love hotel", "tatami room", "public train", "outdoors", "indoors",
    "castle", "temple", "church", "dojo", "cave", "underwater", "stadium", "concert", "bar", "club",
    "rooftop_pool", "hotel_room", "luxury_bathroom", "sauna", "locker_room_shower",
    "night_cityscape", "alleyway", "parking_garage", "abandoned_building", "bridge_over_river",
    # Additional common Danbooru / SDXL environments
    "city_at_night", "city_skyline", "tokyo_street", "shibuya_crossing",
    "train_platform", "subway_car", "amusement_park", "ferris_wheel",
    "arcade", "shopping_mall", "market_street", "festival", "fireworks_view",
    "cliffside", "lakeside", "riverbank", "waterfall", "snowy_forest",
    "blossom_park", "school_hallway", "school_rooftop", "locker_corridor"
]

LIGHTING = [
    "Random",
    "natural sunlight", "golden hour", "soft overcast", "cinematic lighting",
    "studio softbox", "studio_lighting", "hard rim lighting", "rim_lighting", "backlighting",
    "neon lights", "volumetric fog", "dark moody lighting", "dramatic_lighting",
    "moonlight", "bioluminescent glow", "camera flash", "dimly lit", "candlelight",
    "god rays", "lens flare", "soft_lighting", "harsh_lighting", "outdoor_lighting",
    "indoor_lighting", "overcast", "night", "day", "sunset", "sunrise", "silhouette",
    "spotlight", "rimlit_silhouette", "colored_gel_lighting", "club_neon_lighting",
    "hdr_lighting", "dramatic_shadows",
    # Additional nuanced lighting tags
    "soft_shadow", "strong_shadow", "backlit", "front_lighting",
    "side_lighting", "top_lighting", "underlighting", "colored_lighting",
    "pink_neon_lighting", "blue_neon_lighting", "studio_backdrop_lighting"
]

CAMERAS = [
    "Random",
    "85mm portrait lens", "35mm street lens", "24mm wide angle", "50mm standard lens",
    "200mm telephoto", "macro lens", "fisheye lens", "wide_shot", "wide angle view",
    "CCTV footage", "Polaroid style", "GoPro view", "drone shot",
    "from below", "from above", "dutch angle", "close-up", "extreme close-up",
    "cowboy shot", "full body", "full body shot", "upper body", "medium shot",
    "long shot", "bird's eye view", "low angle", "high angle", "over_shoulder",
    "pov", "looking at viewer",
    "closeup_face", "bust_shot", "three_quarter_view", "profile_view",
    "dolly_zoom_feel", "cinematic_framing",
    # Additional composition / camera-angle tags
    "wide_angle_lens", "telephoto_lens", "overhead_shot", "worm's_eye_view",
    "extreme_low_angle", "extreme_high_angle", "shoulder_level_shot",
    "hip_level_shot", "intimate_closeup", "face_focus", "body_focus"
]

SEX_ACTS = [
    "None", "Random",
    "sex", "vaginal sex", "anal sex", "oral sex", "fellatio", "cunnilingus", "sixty-nine",
    "fingering", "handjob", "paizuri", "titfuck", "rimming", "footjob", "thigh job",
    "frottage", "tribadism", "deepthroat", "face fucking", "irrumatio",
    "double penetration", "gangbang", "bukkake", "creampie", "facial", "internal ejaculation",
    "masturbation", "spitroast", "group sex",
    "cum_on_breasts", "cum_on_stomach", "cum_on_thighs", "hand_on_thigh",
    "teasing", "groping_breasts", "groping_butt", "public_sex", "bath_sex"
]

SEX_POSITIONS = [
    "None", "Random",
    "missionary", "doggy style", "cowgirl position", "reverse cowgirl", "mating press",
    "standing sex", "spooning sex", "piledriver", "amazon position", "carried sex",
    "against wall", "on desk", "suspended", "facesitting", "prone bone",
    "legs over shoulders", "lotus position", "bridge position", "bent over",
    "cowgirl_on_chair", "reverse_cowgirl_on_sofa", "standing_doggy", "table_edge_sex",
    "side-by-side_position"
]

NSFW_MODIFIERS = [
    "nude", "naked", "topless", "bottomless", "nipples", "areolae", "pussy juice",
    "sweat", "tears", "blush", "ahegao", "rolling eyes", "tongue out", "drooling",
    "hard nipples", "detailed genitals", "uncensored", "cum on body", "cum on face",
    "messy hair", "heavy breathing",
    "wet_skin", "oil_on_skin", "body_glitter", "thigh_squeeze", "panty_pull_aside",
    "visible_panty_line", "cameltoe", "underboob", "sideboob", "nip_slip",
    # Additional explicit and fetish-leaning modifiers from common SD/Danbooru usage
    "cum_in_mouth", "cum_on_hair", "semen", "dripping_cum", "multiple_cumshots",
    "saliva", "string_of_saliva", "spitstring", "glistening_skin",
    "sweaty_skin", "spread_pussy", "gaping", "pussy_juice_trail",
    "handprint_on_ass", "red_marks_on_skin"
]

# --- HELPER FUNCTIONS ---

def get_smart_random(category_list, seed, exclude_none=True):
    # Filters out 'Random' and 'None' for the selection pool
    pool = [x for x in category_list if x != "Random" and (not exclude_none or x != "None")]
    if not pool:
        return ""
    random.seed(seed)
    return random.choice(pool)

# --- NODES ---

class CR_Pony_Subject:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "gender": (GENDERS, {"default": "female"}),
                "age": (AGES, {"default": "25"}),
                "ethnicity": (ETHNICITIES, {"default": "Caucasian"}),
                "body_type": (ALL_BODY_TYPES, {"default": "slim body"}),
                "skin_texture": (SKIN_TYPES, {"default": "pale skin"}),
                "hair_color": (HAIR_COLORS, {"default": "platinum blonde"}),
                "hair_style": (ALL_HAIRSTYLES, {"default": "messy bun"}),
                "eye_color": (EYE_COLORS, {"default": "blue"}),
                "full_outfit": (FULL_OUTFITS, {"default": "Random"}),
                "top_clothing": (TOP_CLOTHING, {"default": "t-shirt"}),
                "bottom_clothing": (BOTTOM_CLOTHING, {"default": "jeans"}),
                "headwear": (HEADWEAR, {"default": "None"}),
                "shoes": (FOOTWEAR, {"default": "None"}),
                "accessories": (ACCESSORIES, {"default": "None"}),
                "pose": (ALL_POSES, {"default": "standing elegantly"}),
                "breast_size": (BREAST_SIZES, {"default": "medium breasts"}),
                "breast_shape": (BREAST_SHAPES, {"default": "natural breasts"}),
            },
            "optional": {
                "custom_tags": ("STRING", {"multiline": True, "default": ""}),
                "nsfw_modifiers": ("BOOLEAN", {"default": False}),
                "leg_feature": (LEG_FEATURES, {"default": "Random"}),
                "butt_feature": (BUTT_FEATURES, {"default": "Random"}),
                "face_shape": (FACE_SHAPES, {"default": "Random"}),
                "expression": (EXPRESSIONS, {"default": "Random"}),
                "hair_length": (HAIR_LENGTHS, {"default": "Random"}),
                "extra_clothing_tags": ("STRING", {"multiline": True, "default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("subject_prompt",)
    FUNCTION = "generate_subject"
    CATEGORY = "CyberRealistic Pony"

    def generate_subject(self, seed, gender, age, ethnicity, body_type, skin_texture,
                        hair_color, hair_style, eye_color, full_outfit,
                        top_clothing, bottom_clothing, headwear, shoes, accessories,
                        pose, breast_size, breast_shape, custom_tags="", nsfw_modifiers=False,
                        leg_feature="Random", butt_feature="Random",
                        face_shape="Random", expression="Random", hair_length="Random",
                        extra_clothing_tags=""):

        # Seed the RNG
        random.seed(seed)

        # Resolve Randoms
        r_gender = get_smart_random(GENDERS, seed) if gender == "Random" else gender
        r_age = get_smart_random(AGES, seed + 1) if age == "Random" else age
        r_ethnicity = get_smart_random(ETHNICITIES, seed + 2) if ethnicity == "Random" else ethnicity
        r_body = get_smart_random(ALL_BODY_TYPES, seed + 3) if body_type == "Random" else body_type
        r_skin = get_smart_random(SKIN_TYPES, seed + 4) if skin_texture == "Random" else skin_texture
        r_h_color = get_smart_random(HAIR_COLORS, seed + 5) if hair_color == "Random" else hair_color
        r_h_style = get_smart_random(ALL_HAIRSTYLES, seed + 6) if hair_style == "Random" else hair_style
        r_eyes = get_smart_random(EYE_COLORS, seed + 7) if eye_color == "Random" else eye_color
        r_pose = get_smart_random(ALL_POSES, seed + 9) if pose == "Random" else pose

        # Construct Noun
        noun = "woman" if r_gender == "female" else "man" if r_gender == "male" else "person"

        # Construct String (avoid "hair hair" when tag already contains hair, e.g. straight_hair)
        eth_str = f"{r_ethnicity} {noun}" if r_ethnicity != "Caucasian" else noun
        hair_part = "" if "hair" in r_h_style.lower() else " hair"
        prompt = f"({eth_str}, {r_age} years old:1.1), {r_body}, {r_skin}, {r_h_color} {r_h_style}{hair_part}, {r_eyes} eyes"

        # Clothing selection
        clothing_tags = []
        r_full_outfit = get_smart_random(FULL_OUTFITS, seed + 8) if full_outfit == "Random" else full_outfit
        if r_full_outfit and r_full_outfit not in ["Random", "None"]:
            clothing_tags.append(r_full_outfit)

        def _resolve_choice(choice, data, offset):
            if choice is None:
                return None
            if choice == "Random":
                return get_smart_random(data, seed + offset)
            return choice

        r_top = _resolve_choice(top_clothing, TOP_CLOTHING, 12)
        r_bottom = _resolve_choice(bottom_clothing, BOTTOM_CLOTHING, 13)
        r_head = _resolve_choice(headwear, HEADWEAR, 14)
        r_shoes = _resolve_choice(shoes, FOOTWEAR, 15)
        r_acc = _resolve_choice(accessories, ACCESSORIES, 16)

        for item in [r_top, r_bottom, r_head, r_shoes, r_acc]:
            if item and item not in ["Random", "None"]:
                clothing_tags.append(item)

        if clothing_tags:
            prompt += f", wearing {', '.join(clothing_tags)}"

        # Pose
        prompt += f", {r_pose}"

        # Breasts (Only if not male)
        if r_gender != "male":
            r_b_size = get_smart_random(BREAST_SIZES, seed + 10) if breast_size == "Random" else breast_size
            r_b_shape = get_smart_random(BREAST_SHAPES, seed + 11) if breast_shape == "Random" else breast_shape
            if r_b_size and r_b_size != "None":
                prompt += f", {r_b_size}"
            if r_b_shape and r_b_shape != "None":
                prompt += f", {r_b_shape}"

        # Extra body-part controls
        def _resolve_feature(choice, data, offset):
            if not choice:
                return None
            if choice == "Random":
                return get_smart_random(data, seed + offset)
            return choice

        r_leg = _resolve_feature(leg_feature, LEG_FEATURES, 17)
        r_butt = _resolve_feature(butt_feature, BUTT_FEATURES, 18)
        r_face = _resolve_feature(face_shape, FACE_SHAPES, 19)
        r_expr = _resolve_feature(expression, EXPRESSIONS, 20)
        r_hlen = _resolve_feature(hair_length, HAIR_LENGTHS, 21)

        for feat in [r_leg, r_butt, r_face, r_expr, r_hlen]:
            if feat and feat not in ["Random", "None"]:
                prompt += f", {feat}"

        # Extra Clothing & Custom Tags at the end
        if extra_clothing_tags.strip():
            prompt += f", {extra_clothing_tags.strip()}"
        if custom_tags.strip():
            prompt += f", {custom_tags.strip()}"

        # NSFW Auto-Modifiers
        if nsfw_modifiers:
            mods = random.sample(NSFW_MODIFIERS, 2)
            prompt += f", {', '.join(mods)}"
            if r_gender == "male":
                prompt += ", penis, balls"
            elif r_gender == "female":
                prompt += ", pussy"

        return (prompt,)


class CR_Pony_Subject_Female:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "age": (AGES, {"default": "25"}),
                "ethnicity": (ETHNICITIES, {"default": "Caucasian"}),
                "body_type": (FEMALE_BODY_TYPES, {"default": "slim body"}),
                "skin_texture": (SKIN_TYPES, {"default": "pale skin"}),
                "hair_color": (HAIR_COLORS, {"default": "platinum blonde"}),
                "hair_style": (FEMALE_HAIRSTYLES, {"default": "messy bun"}),
                "eye_color": (EYE_COLORS, {"default": "blue"}),
                "full_outfit": (FULL_OUTFITS, {"default": "Random"}),
                "top_clothing": (FEMALE_TOP_CLOTHING, {"default": "t-shirt"}),
                "bottom_clothing": (BOTTOM_CLOTHING, {"default": "jeans"}),
                "headwear": (HEADWEAR, {"default": "None"}),
                "shoes": (FOOTWEAR, {"default": "None"}),
                "accessories": (ACCESSORIES, {"default": "None"}),
                "pose": (ALL_POSES, {"default": "standing elegantly"}),
                "breast_size": (BREAST_SIZES, {"default": "medium breasts"}),
                "breast_shape": (BREAST_SHAPES, {"default": "natural breasts"}),
            },
            "optional": {
                "custom_tags": ("STRING", {"multiline": True, "default": ""}),
                "nsfw_modifiers": ("BOOLEAN", {"default": False}),
                "leg_feature": (LEG_FEATURES, {"default": "Random"}),
                "butt_feature": (BUTT_FEATURES, {"default": "Random"}),
                "face_shape": (FACE_SHAPES, {"default": "Random"}),
                "expression": (EXPRESSIONS, {"default": "Random"}),
                "hair_length": (HAIR_LENGTHS, {"default": "Random"}),
                "extra_clothing_tags": ("STRING", {"multiline": True, "default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("subject_prompt",)
    FUNCTION = "generate_subject"
    CATEGORY = "CyberRealistic Pony"

    def generate_subject(self, seed, age, ethnicity, body_type, skin_texture,
                        hair_color, hair_style, eye_color, full_outfit,
                        top_clothing, bottom_clothing, headwear, shoes, accessories,
                        pose, breast_size, breast_shape, custom_tags="", nsfw_modifiers=False,
                        leg_feature="Random", butt_feature="Random",
                        face_shape="Random", expression="Random", hair_length="Random",
                        extra_clothing_tags=""):

        # Seed the RNG
        random.seed(seed)

        r_gender = "female"
        r_age = get_smart_random(AGES, seed + 1) if age == "Random" else age
        r_ethnicity = get_smart_random(ETHNICITIES, seed + 2) if ethnicity == "Random" else ethnicity
        r_body = get_smart_random(FEMALE_BODY_TYPES, seed + 3) if body_type == "Random" else body_type
        r_skin = get_smart_random(SKIN_TYPES, seed + 4) if skin_texture == "Random" else skin_texture
        r_h_color = get_smart_random(HAIR_COLORS, seed + 5) if hair_color == "Random" else hair_color
        r_h_style = get_smart_random(FEMALE_HAIRSTYLES, seed + 6) if hair_style == "Random" else hair_style
        r_eyes = get_smart_random(EYE_COLORS, seed + 7) if eye_color == "Random" else eye_color
        r_pose = get_smart_random(ALL_POSES, seed + 9) if pose == "Random" else pose

        noun = "woman"
        eth_str = f"{r_ethnicity} {noun}" if r_ethnicity != "Caucasian" else noun
        hair_part = "" if "hair" in r_h_style.lower() else " hair"
        prompt = f"({eth_str}, {r_age} years old:1.1), {r_body}, {r_skin}, {r_h_color} {r_h_style}{hair_part}, {r_eyes} eyes"

        clothing_tags = []
        r_full_outfit = get_smart_random(FULL_OUTFITS, seed + 8) if full_outfit == "Random" else full_outfit
        if r_full_outfit and r_full_outfit not in ["Random", "None"]:
            clothing_tags.append(r_full_outfit)

        def _resolve_choice(choice, data, offset):
            if choice is None:
                return None
            if choice == "Random":
                return get_smart_random(data, seed + offset)
            return choice

        r_top = _resolve_choice(top_clothing, FEMALE_TOP_CLOTHING, 12)
        r_bottom = _resolve_choice(bottom_clothing, BOTTOM_CLOTHING, 13)
        r_head = _resolve_choice(headwear, HEADWEAR, 14)
        r_shoes = _resolve_choice(shoes, FOOTWEAR, 15)
        r_acc = _resolve_choice(accessories, ACCESSORIES, 16)

        for item in [r_top, r_bottom, r_head, r_shoes, r_acc]:
            if item and item not in ["Random", "None"]:
                clothing_tags.append(item)

        if clothing_tags:
            prompt += f", wearing {', '.join(clothing_tags)}"

        prompt += f", {r_pose}"

        # Breasts (always applicable here)
        r_b_size = get_smart_random(BREAST_SIZES, seed + 10) if breast_size == "Random" else breast_size
        r_b_shape = get_smart_random(BREAST_SHAPES, seed + 11) if breast_shape == "Random" else breast_shape
        if r_b_size and r_b_size != "None":
            prompt += f", {r_b_size}"
        if r_b_shape and r_b_shape != "None":
            prompt += f", {r_b_shape}"

        def _resolve_feature(choice, data, offset):
            if not choice:
                return None
            if choice == "Random":
                return get_smart_random(data, seed + offset)
            return choice

        r_leg = _resolve_feature(leg_feature, LEG_FEATURES, 17)
        r_butt = _resolve_feature(butt_feature, BUTT_FEATURES, 18)
        r_face = _resolve_feature(face_shape, FACE_SHAPES, 19)
        r_expr = _resolve_feature(expression, EXPRESSIONS, 20)
        r_hlen = _resolve_feature(hair_length, HAIR_LENGTHS, 21)

        for feat in [r_leg, r_butt, r_face, r_expr, r_hlen]:
            if feat and feat not in ["Random", "None"]:
                prompt += f", {feat}"

        if extra_clothing_tags.strip():
            prompt += f", {extra_clothing_tags.strip()}"
        if custom_tags.strip():
            prompt += f", {custom_tags.strip()}"

        if nsfw_modifiers:
            mods = random.sample(NSFW_MODIFIERS, 2)
            prompt += f", {', '.join(mods)}"
            prompt += ", pussy"

        return (prompt,)


class CR_Pony_Subject_Male:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "age": (AGES, {"default": "25"}),
                "ethnicity": (ETHNICITIES, {"default": "Caucasian"}),
                "body_type": (MALE_BODY_TYPES, {"default": "athletic_male"}),
                "skin_texture": (SKIN_TYPES, {"default": "pale skin"}),
                "hair_color": (HAIR_COLORS, {"default": "black"}),
                "hair_style": (MALE_HAIRSTYLES, {"default": "fade"}),
                "eye_color": (EYE_COLORS, {"default": "blue"}),
                "full_outfit": (FULL_OUTFITS, {"default": "Random"}),
                "top_clothing": (MALE_TOP_CLOTHING, {"default": "t-shirt"}),
                "bottom_clothing": (BOTTOM_CLOTHING, {"default": "jeans"}),
                "headwear": (HEADWEAR, {"default": "None"}),
                "shoes": (FOOTWEAR, {"default": "None"}),
                "accessories": (ACCESSORIES, {"default": "None"}),
                "pose": (ALL_POSES, {"default": "standing confidently"}),
            },
            "optional": {
                "custom_tags": ("STRING", {"multiline": True, "default": ""}),
                "nsfw_modifiers": ("BOOLEAN", {"default": False}),
                "leg_feature": (LEG_FEATURES, {"default": "Random"}),
                "butt_feature": (BUTT_FEATURES, {"default": "Random"}),
                "face_shape": (FACE_SHAPES, {"default": "Random"}),
                "expression": (EXPRESSIONS, {"default": "Random"}),
                "hair_length": (HAIR_LENGTHS, {"default": "Random"}),
                "extra_clothing_tags": ("STRING", {"multiline": True, "default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("subject_prompt",)
    FUNCTION = "generate_subject"
    CATEGORY = "CyberRealistic Pony"

    def generate_subject(self, seed, age, ethnicity, body_type, skin_texture,
                        hair_color, hair_style, eye_color, full_outfit,
                        top_clothing, bottom_clothing, headwear, shoes, accessories,
                        pose, custom_tags="", nsfw_modifiers=False,
                        leg_feature="Random", butt_feature="Random",
                        face_shape="Random", expression="Random", hair_length="Random",
                        extra_clothing_tags=""):

        random.seed(seed)

        r_gender = "male"
        r_age = get_smart_random(AGES, seed + 1) if age == "Random" else age
        r_ethnicity = get_smart_random(ETHNICITIES, seed + 2) if ethnicity == "Random" else ethnicity
        r_body = get_smart_random(MALE_BODY_TYPES, seed + 3) if body_type == "Random" else body_type
        r_skin = get_smart_random(SKIN_TYPES, seed + 4) if skin_texture == "Random" else skin_texture
        r_h_color = get_smart_random(HAIR_COLORS, seed + 5) if hair_color == "Random" else hair_color
        r_h_style = get_smart_random(MALE_HAIRSTYLES, seed + 6) if hair_style == "Random" else hair_style
        r_eyes = get_smart_random(EYE_COLORS, seed + 7) if eye_color == "Random" else eye_color
        r_pose = get_smart_random(ALL_POSES, seed + 9) if pose == "Random" else pose

        noun = "man"
        eth_str = f"{r_ethnicity} {noun}" if r_ethnicity != "Caucasian" else noun
        hair_part = "" if "hair" in r_h_style.lower() else " hair"
        prompt = f"({eth_str}, {r_age} years old:1.1), {r_body}, {r_skin}, {r_h_color} {r_h_style}{hair_part}, {r_eyes} eyes"

        clothing_tags = []
        r_full_outfit = get_smart_random(FULL_OUTFITS, seed + 8) if full_outfit == "Random" else full_outfit
        if r_full_outfit and r_full_outfit not in ["Random", "None"]:
            clothing_tags.append(r_full_outfit)

        def _resolve_choice(choice, data, offset):
            if choice is None:
                return None
            if choice == "Random":
                return get_smart_random(data, seed + offset)
            return choice

        r_top = _resolve_choice(top_clothing, MALE_TOP_CLOTHING, 12)
        r_bottom = _resolve_choice(bottom_clothing, BOTTOM_CLOTHING, 13)
        r_head = _resolve_choice(headwear, HEADWEAR, 14)
        r_shoes = _resolve_choice(shoes, FOOTWEAR, 15)
        r_acc = _resolve_choice(accessories, ACCESSORIES, 16)

        for item in [r_top, r_bottom, r_head, r_shoes, r_acc]:
            if item and item not in ["Random", "None"]:
                clothing_tags.append(item)

        if clothing_tags:
            prompt += f", wearing {', '.join(clothing_tags)}"

        prompt += f", {r_pose}"

        def _resolve_feature(choice, data, offset):
            if not choice:
                return None
            if choice == "Random":
                return get_smart_random(data, seed + offset)
            return choice

        r_leg = _resolve_feature(leg_feature, LEG_FEATURES, 17)
        r_butt = _resolve_feature(butt_feature, BUTT_FEATURES, 18)
        r_face = _resolve_feature(face_shape, FACE_SHAPES, 19)
        r_expr = _resolve_feature(expression, EXPRESSIONS, 20)
        r_hlen = _resolve_feature(hair_length, HAIR_LENGTHS, 21)

        for feat in [r_leg, r_butt, r_face, r_expr, r_hlen]:
            if feat and feat not in ["Random", "None"]:
                prompt += f", {feat}"

        if extra_clothing_tags.strip():
            prompt += f", {extra_clothing_tags.strip()}"
        if custom_tags.strip():
            prompt += f", {custom_tags.strip()}"

        if nsfw_modifiers:
            mods = random.sample(NSFW_MODIFIERS, 2)
            prompt += f", {', '.join(mods)}"
            prompt += ", penis, balls"

        return (prompt,)

class CR_Pony_Master:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "rating": (RATINGS, {"default": "rating_safe"}),
                "location": (LOCATIONS, {"default": "luxury penthouse"}),
                "lighting": (LIGHTING, {"default": "cinematic lighting"}),
                "camera": (CAMERAS, {"default": "85mm portrait lens"}),
                "use_break": ("BOOLEAN", {"default": True}),
                "nsfw_mode": ("BOOLEAN", {"default": False}),
            },
            "optional": {
                "sex_act": (SEX_ACTS, {"default": "None"}),
                "sex_position": (SEX_POSITIONS, {"default": "None"}),
                "score_scheme": (SCORE_SCHEMES, {"default": "default high"}),
                "source_bias": (SOURCE_TAGS, {"default": "None"}),
                "strong_anime_bias": ("BOOLEAN", {"default": False}),
                "style_preset": (STYLE_PRESETS, {"default": "None"}),
                "subject_1": ("STRING", {"forceInput": True}),
                "subject_2": ("STRING", {"forceInput": True}),
                "subject_3": ("STRING", {"forceInput": True}),
                "subject_4": ("STRING", {"forceInput": True}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_prompt")
    FUNCTION = "generate_master"
    CATEGORY = "CyberRealistic Pony"

    def generate_master(self, seed, rating, location, lighting, camera, use_break, nsfw_mode,
                       sex_act="None", sex_position="None",
                       score_scheme="default high", source_bias="None", strong_anime_bias=False,
                       style_preset="None",
                       subject_1=None, subject_2=None, subject_3=None, subject_4=None):

        random.seed(seed)

        # 1. Header
        if score_scheme == "score_9 only":
            base_score = "score_9"
        elif score_scheme == "score_7_plus":
            base_score = "score_9, score_8_up, score_7_up"
        else:
            base_score = "score_9, score_8_up, score_7_up, score_6_up"

        # Quality/source handling
        # Default photography bias; source_bias can override or add to this.
        quality = "raw photo, hyperrealistic, 8k uhd, film grain, masterpiece, highly detailed"
        source_tags = []
        if source_bias and source_bias != "None":
            source_tags.append(source_bias)
        else:
            source_tags.append("source_photography")

        # Style presets inject small curated bundles
        style_tags = []
        if style_preset == "photorealistic":
            style_tags.append("photo-realistic")
        elif style_preset == "anime_leaning":
            style_tags.append("anime style, soft shading")
        elif style_preset == "sketch":
            style_tags.append("pencil sketch, lineart emphasis")
        elif style_preset == "studio_glamour":
            style_tags.append("studio glamour, beauty lighting")

        header_parts = [base_score, rating, ", ".join(source_tags), quality]
        if style_tags:
            header_parts.append(", ".join(style_tags))
        pos = f"{', '.join(header_parts)}, "

        # 2. Sex Acts (NSFW) — appear early in prompt, weighted by scheme
        if nsfw_mode:
            r_act = get_smart_random(SEX_ACTS, seed + 3, exclude_none=True) if sex_act == "Random" else sex_act
            r_pos = get_smart_random(SEX_POSITIONS, seed + 4, exclude_none=True) if sex_position == "Random" else sex_position
            if score_scheme == "default high":
                act_weight = "3"
                pos_weight = "3"
            else:
                act_weight = "1.2"
                pos_weight = "1.15"
            if r_act and r_act != "None":
                pos += f"({r_act}:{act_weight}), "
            if r_pos and r_pos != "None":
                pos += f"({r_pos}:{pos_weight}), "

        # 3. Count Logic & Subject Collection (only add count tags that match actual subjects)
        subjects = [s for s in [subject_1, subject_2, subject_3, subject_4] if s and str(s).strip()]
        count = len(subjects)

        # Count by gender: avoid "man" matching inside "woman"
        def _is_girl(s):
            return "woman" in s or "girl" in s
        def _is_boy(s):
            return "boy" in s or ("man" in s and "woman" not in s)
        girl_count = sum(1 for s in subjects if _is_girl(s))
        boy_count = sum(1 for s in subjects if _is_boy(s))

        if count == 0:
            pass  # no count tags when no subjects
        elif count == 1:
            if girl_count == 1:
                pos += "1girl, "
            elif boy_count == 1:
                pos += "1boy, "
            else:
                pos += "1person, "
        elif count == 2:
            if girl_count == 2:
                pos += "2girls, "
            elif boy_count == 2:
                pos += "2boys, "
            elif girl_count == 1 and boy_count == 1:
                pos += "1girl, 1boy, "
            else:
                pos += "2people, "
        else:
            pos += f"{count}people, "

        # 4. Scene — before subject strings
        r_loc = get_smart_random(LOCATIONS, seed) if location == "Random" else location
        r_light = get_smart_random(LIGHTING, seed + 1) if lighting == "Random" else lighting
        r_cam = get_smart_random(CAMERAS, seed + 2) if camera == "Random" else camera
        pos += f"{r_loc}, {r_light}, {r_cam}"

        # 5. Subject Assembly
        if count > 0:
            pos += ", "
        for i, subj in enumerate(subjects):
            pos += subj
            if use_break and i < count - 1:
                pos += " BREAK "
            elif i < count - 1:
                pos += ", "
        # 6. Negative Prompt
        neg_sources = ["source_furry", "source_cartoon"]
        # strong_anime_bias: flip anime-ish tags toward positive look, relax them in negative
        if strong_anime_bias:
            # Drop explicit anime/cartoon negatives
            neg_sources = ["source_furry"]

        neg = f"score_4, score_5, score_6, {', '.join(neg_sources)}, 3d, illustration, sketch, painting, cartoon, anime, grayscale, monochrome, text, watermark"
        if not nsfw_mode:
            neg += ", nude, nipples, pussy, penis, sex, nsfw"

        return (pos, neg)

# --- MAPPINGS ---

NODE_CLASS_MAPPINGS = {
    "CR_Pony_Master": CR_Pony_Master,
    "CR_Pony_Subject": CR_Pony_Subject,
    "CR_Pony_Subject_Female": CR_Pony_Subject_Female,
    "CR_Pony_Subject_Male": CR_Pony_Subject_Male,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CR_Pony_Master": "CyberRealistic Master Prompt",
    "CR_Pony_Subject": "CyberRealistic Subject",
    "CR_Pony_Subject_Female": "CyberRealistic Female Subject",
    "CR_Pony_Subject_Male": "CyberRealistic Male Subject",
}
