import random

# --- DATA CONSTANTS (Ported from the Web App) ---

GENDERS = ["female", "male", "futa", "other", "Random"]
RATINGS = ["rating_safe", "rating_questionable", "rating_explicit"]

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

ALL_CLOTHING = [
    "Random",
    "nude", "lingerie", "lace underwear", "bikini", "micro bikini", "one-piece swimsuit",
    "shell_bikini", "frilled_swimsuit", "front_zipper_swimsuit", "bikesuit", "wrestling_outfit",
    "evening_gown", "evening gown", "cocktail_dress", "cocktail dress", "gown", "wedding_dress",
    "canonicals", "sundress", "summer dress", "sleeveless_dress", "strapless_dress", "backless_dress",
    "halter_dress", "sailor_dress", "pinafore_dress", "frilled_dress", "sweater_dress",
    "pleated_dress", "pencil_dress", "cheongsam", "china_dress", "off-shoulder_dress",
    "armored_dress", "fur-trimmed_dress", "lace-trimmed_dress", "collared_dress", "layered_dress",
    "multicolored_dress", "striped_dress", "checkered_skirt", "polka_dot_dress", "plaid_dress",
    "print_dress", "ribbed_dress", "short_jumpsuit", "maid", "miko", "school_uniform", "sailor",
    "serafuku", "sailor_senshi_uniform", "summer_uniform", "naval_uniform", "military_uniform",
    "business_suit", "business suit", "nurse", "chef_uniform", "labcoat", "cheerleader",
    "band_uniform", "space_suit", "leotard", "domineering", "hanbok", "japanese_clothes",
    "chinese_style", "traditional_clothes", "uchikake", "sleeveless_kimono", "print_kimono",
    "hanten_(clothes)", "korean_clothes", "gothic", "lolita", "gothic_lolita", "byzantine_fashion",
    "tropical cloth", "indian_style", "Ao_Dai", "ainu_clothes", "arabian_clothes", "egyptian_clothes",
    "hawaii costume", "furisode", "animal_costume", "bunny_costume", "cat_costume", "santa_costume",
    "hoodie", "pajamas", "nightgown", "sleepwear", "print_pajamas", "yukata", "hanfu", "Taoist robe",
    "robe", "cloak", "hooded_cloak", "winter_clothes", "down jacket", "halloween_costume", "loungewear",
    "santa", "harem_outfit", "shrug_clothing", "gym_uniform", "athletic_leotard", "volleyball_uniform",
    "tennis_uniform", "baseball_uniform", "letterman_jacket", "biker_clothes",
    "t-shirt", "blouse", "off-shoulder_shirt", "collared_shirt", "collared shirt", "dress_shirt",
    "sailor_shirt", "cropped_shirt", "criss-cross_halter", "frilled_shirt", "sweatshirt",
    "hawaiian_shirt", "kappougi", "polo_shirt", "polo shirt", "print_shirt", "sleeveless_hoodie",
    "sleeveless_shirt", "striped_shirt", "tank_top", "tank top", "vest", "waistcoat", "cardigan",
    "sweater", "virgin killer sweater", "hooded_sweater", "striped_sweater", "pullover_sweaters",
    "ribbed_sweater", "sweater_vest", "backless_sweater", "blazer", "overcoat", "double-breasted",
    "long_coat", "winter_coat", "hooded_coat", "fur_coat", "fur-trimmed_coat", "duffel_coat",
    "parka", "cropped_jacket", "track_jacket", "hooded_track_jacket", "military_jacket",
    "camouflage_jacket", "leather_jacket", "leather jacket", "trench_coat", "windbreaker", "raincoat",
    "tunic", "cape", "capelet", "hagoromo", "waist_apron", "maid_apron", "clothes_around_waist",
    "jacket_around_waist", "sweater_around_waist", "loincloth", "corset", "bustier", "girdle",
    "armor", "bikini_armor", "full_armor", "plate_armor", "japanese_armor", "kusazuri",
    "power_armor", "helmet", "kabuto", "off-shoulder_armor", "shoulder_armor", "muneate",
    "breastplate", "faulds", "skirt", "miniskirt", "mini_skirt", "skirt_suit", "bikini_skirt",
    "pleated_skirt", "pencil_skirt", "bubble_skirt", "tutu", "ballgown", "denim_skirt",
    "suspender_skirt", "long_skirt", "high-waist_skirt", "chiffon_skirt", "lace_skirt",
    "layered_skirt", "print_skirt", "flared_skirt", "floral_skirt", "jumpsuit", "hot_pants",
    "striped_shorts", "suspender_shorts", "denim_shorts", "puffy_shorts", "dolphin_shorts",
    "tight pants", "yoga pants", "track_pants", "bike_shorts", "gym_shorts", "pants",
    "puffy_pants", "pumpkin_pants", "hakama", "hakama_pants", "harem_pants", "bloomers", "buruma",
    "jeans", "cargo_pants", "camouflage_pants", "capri_pants", "chaps", "plaid_pants",
    "striped_pants", "torn_jeans", "boxers", "briefs", "swim trunks", "tuxedo", "tailored suit",
    "fishnets", "thighhighs", "latex bodysuit", "towel", "apron", "harness", "rigging",
    "lab coat", "mechanic jumpsuit", "biker vest", "streetwear", "casual", "cyberpunk techwear"
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
    "medium build", "skinny", "stocky", "obese", "toned"
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
    "profile", "back to viewer", "reclining", "standing on one leg"
]

BREAST_SIZES = [
    "Random", "None", "flat chest", "small breasts", "medium breasts", "large breasts",
    "huge breasts", "gigantic breasts", "massive breasts"
]

BREAST_SHAPES = [
    "Random", "None", "natural breasts", "perky breasts", "saggy breasts", "asymmetrical breasts",
    "perfect breasts", "heavy breasts"
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
    "castle", "temple", "church", "dojo", "cave", "underwater", "stadium", "concert", "bar", "club"
]

LIGHTING = [
    "Random",
    "natural sunlight", "golden hour", "soft overcast", "cinematic lighting",
    "studio softbox", "studio_lighting", "hard rim lighting", "rim_lighting", "backlighting",
    "neon lights", "volumetric fog", "dark moody lighting", "dramatic_lighting",
    "moonlight", "bioluminescent glow", "camera flash", "dimly lit", "candlelight",
    "god rays", "lens flare", "soft_lighting", "harsh_lighting", "outdoor_lighting",
    "indoor_lighting", "overcast", "night", "day", "sunset", "sunrise", "silhouette"
]

CAMERAS = [
    "Random",
    "85mm portrait lens", "35mm street lens", "24mm wide angle", "50mm standard lens",
    "200mm telephoto", "macro lens", "fisheye lens", "wide_shot", "wide angle view",
    "CCTV footage", "Polaroid style", "GoPro view", "drone shot",
    "from below", "from above", "dutch angle", "close-up", "extreme close-up",
    "cowboy shot", "full body", "full body shot", "upper body", "medium shot",
    "long shot", "bird's eye view", "low angle", "high angle", "over_shoulder",
    "pov", "looking at viewer"
]

SEX_ACTS = [
    "None", "Random",
    "sex", "vaginal sex", "anal sex", "oral sex", "fellatio", "cunnilingus", "sixty-nine",
    "fingering", "handjob", "paizuri", "titfuck", "rimming", "footjob", "thigh job",
    "frottage", "tribadism", "deepthroat", "face fucking", "irrumatio",
    "double penetration", "gangbang", "bukkake", "creampie", "facial", "internal ejaculation",
    "masturbation", "spitroast", "group sex"
]

SEX_POSITIONS = [
    "None", "Random",
    "missionary", "doggy style", "cowgirl position", "reverse cowgirl", "mating press",
    "standing sex", "spooning sex", "piledriver", "amazon position", "carried sex",
    "against wall", "on desk", "suspended", "facesitting", "prone bone",
    "legs over shoulders", "lotus position", "bridge position", "bent over"
]

NSFW_MODIFIERS = [
    "nude", "naked", "topless", "bottomless", "nipples", "areolae", "pussy juice",
    "sweat", "tears", "blush", "ahegao", "rolling eyes", "tongue out", "drooling",
    "hard nipples", "detailed genitals", "uncensored", "cum on body", "cum on face",
    "messy hair", "heavy breathing"
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
                "clothing": (ALL_CLOTHING, {"default": "evening gown"}),
                "pose": (ALL_POSES, {"default": "standing elegantly"}),
                "breast_size": (BREAST_SIZES, {"default": "medium breasts"}),
                "breast_shape": (BREAST_SHAPES, {"default": "natural breasts"}),
            },
            "optional": {
                "custom_tags": ("STRING", {"multiline": True, "default": ""}),
                "nsfw_modifiers": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("subject_prompt",)
    FUNCTION = "generate_subject"
    CATEGORY = "CyberRealistic Pony"

    def generate_subject(self, seed, gender, age, ethnicity, body_type, skin_texture,
                        hair_color, hair_style, eye_color, clothing, pose,
                        breast_size, breast_shape, custom_tags="", nsfw_modifiers=False):

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
        r_clothes = get_smart_random(ALL_CLOTHING, seed + 8) if clothing == "Random" else clothing
        r_pose = get_smart_random(ALL_POSES, seed + 9) if pose == "Random" else pose

        # Construct Noun
        noun = "woman" if r_gender == "female" else "man" if r_gender == "male" else "person"

        # Construct String (avoid "hair hair" when tag already contains hair, e.g. straight_hair)
        eth_str = f"{r_ethnicity} {noun}" if r_ethnicity != "Caucasian" else noun
        hair_part = "" if "hair" in r_h_style.lower() else " hair"
        prompt = f"({eth_str}, {r_age} years old:1.1), {r_body}, {r_skin}, {r_h_color} {r_h_style}{hair_part}, {r_eyes} eyes, wearing {r_clothes}, {r_pose}"

        # Breasts (Only if not male)
        if r_gender != "male":
            r_b_size = get_smart_random(BREAST_SIZES, seed + 10) if breast_size == "Random" else breast_size
            r_b_shape = get_smart_random(BREAST_SHAPES, seed + 11) if breast_shape == "Random" else breast_shape
            if r_b_size and r_b_size != "None":
                prompt += f", {r_b_size}"
            if r_b_shape and r_b_shape != "None":
                prompt += f", {r_b_shape}"

        # Custom Tags
        if custom_tags.strip():
            prompt += f", {custom_tags}"

        # NSFW Auto-Modifiers
        if nsfw_modifiers:
            mods = random.sample(NSFW_MODIFIERS, 2)
            prompt += f", {', '.join(mods)}"
            if r_gender == "male":
                prompt += ", penis, balls"
            elif r_gender == "female":
                prompt += ", pussy"

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
                       subject_1=None, subject_2=None, subject_3=None, subject_4=None):

        random.seed(seed)

        # 1. Header
        base_score = "score_9, score_8_up, score_7_up, score_6_up"
        quality = "source_photography, raw photo, hyperrealistic, 8k uhd, film grain, masterpiece, highly detailed"
        pos = f"{base_score}, {rating}, {quality}, "

        # 2. Count Logic & Subject Collection (only add count tags that match actual subjects)
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

        # 3. Subject Assembly
        for i, subj in enumerate(subjects):
            pos += subj
            if use_break and i < count - 1:
                pos += " BREAK "
            elif i < count - 1:
                pos += ", "

        # 4. Scene
        if use_break and count > 0:
            pos += " BREAK "
        elif count > 0:
            pos += ", "

        r_loc = get_smart_random(LOCATIONS, seed) if location == "Random" else location
        r_light = get_smart_random(LIGHTING, seed + 1) if lighting == "Random" else lighting
        r_cam = get_smart_random(CAMERAS, seed + 2) if camera == "Random" else camera
        pos += f"{r_loc}, {r_light}, {r_cam}"

        # 5. Sex Acts (NSFW)
        if nsfw_mode:
            r_act = get_smart_random(SEX_ACTS, seed + 3, exclude_none=True) if sex_act == "Random" else sex_act
            r_pos = get_smart_random(SEX_POSITIONS, seed + 4, exclude_none=True) if sex_position == "Random" else sex_position
            if r_act and r_act != "None":
                pos += f", {r_act}"
            if r_pos and r_pos != "None":
                pos += f", {r_pos}"

        # 6. Negative Prompt
        neg = "score_4, score_5, score_6, source_anime, source_cartoon, source_furry, 3d, illustration, sketch, painting, cartoon, anime, grayscale, monochrome, text, watermark"
        if not nsfw_mode:
            neg += ", nude, nipples, pussy, penis, sex, nsfw"

        return (pos, neg)

# --- MAPPINGS ---

NODE_CLASS_MAPPINGS = {
    "CR_Pony_Master": CR_Pony_Master,
    "CR_Pony_Subject": CR_Pony_Subject
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CR_Pony_Master": "CyberRealistic Master Prompt",
    "CR_Pony_Subject": "CyberRealistic Subject"
}
