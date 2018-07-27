#!/usr/bin/python3
# -*- coding: utf-8 -*-

INDEPENDENT_VOWELS = [
                'अ', #0x905, # DEVANAGARI LETTER A 
                'आ', #0x906, # DEVANAGARI LETTER AA
                'इ', #0x907, # DEVANAGARI LETTER I
                'ई', #0x908, # DEVANAGARI LETTER II
                'उ', #0x909, # DEVANAGARI LETTER U
                'ऊ', #0x90A, # DEVANAGARI LETTER UU
                'ऋ', #0x90B, # DEVANAGARI LETTER VOCALIC R                
                'ए', #0x90F, # DEVANAGARI LETTER E
                'ऐ', #0x910, # DEVANAGARI LETTER AI                        
                'ओ', #0x913, # DEVANAGARI LETTER O
                'औ', #0x914, # DEVANAGARI LETTER AU
]

INDEPENDENT_VOWELS_ADVANCED = [
                'ऄ', #0x904, # DEVANAGARI LETTER SHORT A • used for short e in Awadhi • also used in Devanagari transliterations of some South Indian and Kashmiri languages by a publisher in Lucknow
                'ऒ', #0x912, # DEVANAGARI LETTER SHORT O • Kashmiri, Bihari languages • also used for transcribing Dravidian short o
                'ऎ', #0x90E, # DEVANAGARI LETTER SHORT E • Kashmiri, Bihari languages • also used for transcribing Dravidian short e
# Independent vowel for Marathi
                'ॲ', #0x972, # DEVANAGARI LETTER CANDRA A  
                'ऑ', #0x911, # DEVANAGARI LETTER CANDRA O 
                'ऍ', #0x90D, # DEVANAGARI LETTER CANDRA E                     
# Additional vowels for Sanskrit
                'ॠ', #0x960, # DEVANAGARI LETTER VOCALIC RR
                'ऌ', #0x90C, # DEVANAGARI LETTER VOCALIC L
                'ॡ', #0x961, # DEVANAGARI LETTER VOCALIC LL                        
# These independent vowels are used in Kashmiri and in the Bihari languages.
                'ॳ', #0x973, # DEVANAGARI LETTER OE
                'ॴ', #0x974, # DEVANAGARI LETTER OOE
                'ॵ', #0x975, # DEVANAGARI LETTER AW
# Independent vowels for Kashmiri
                'ॶ', #0x976, # DEVANAGARI LETTER UE
                'ॷ', #0x977 # DEVANAGARI LETTER UUE
]

SIGNS = [
                'ऀ', #0x900, # DEVANAGARI SIGN INVERTED CANDRABINDU = vaidika adhomukha candrabindu
                'ँ', #0x901, # DEVANAGARI SIGN CANDRABINDU = anunasika →  $̐  combining candrabindu
                'ं', #0x902, # DEVANAGARI SIGN ANUSVARA = bindu
                'ः' #0x903, # DEVANAGARI SIGN VISARGA 
                '़', #0x93C, # DEVANAGARI SIGN NUKTA • for extending the alphabet to new letters
# Abbreviation sign
                '॰', #0x970, # DEVANAGARI ABBREVIATION SIGN • intended for Devanagari-specific abbreviations
                'ॱ', #0x971, # DEVANAGARI SIGN HIGH SPACING DOT
                '्', #0x94D, # DEVANAGARI SIGN VIRAMA = halant (the preferred Hindi name) • suppresses inherent vowel
                '₹' # hindi rupee 
]

PUNCTUATIONS = [
                '।', #0x964, # DEVANAGARI DANDA = purna viram • phrase separator
                '“', # LEFT DOUBLE QUOTATION MARK
                '”', # RIGHT DOUBLE QUOTATION MARK
                '‘', # LEFT SINGLE QUOTATION MARK
                '–', # HYPHEN
                '’' # RIGHT SINGLE QUOTATION MARK
]

CONSONANTS = [
                'क', #0x915, # DEVANAGARI LETTER KA
                'ख', #0x916, # DEVANAGARI LETTER KHA
                'ग', #0x917, # DEVANAGARI LETTER GA
                'घ', #0x918, # DEVANAGARI LETTER GHA
                'ङ', #0x919, # DEVANAGARI LETTER NGA
                'च', #0x91A, # DEVANAGARI LETTER CA
                'छ', #0x91B, # DEVANAGARI LETTER CHA
                'ज', #0x91C, # DEVANAGARI LETTER JA
                'झ', #0x91D, # DEVANAGARI LETTER JHA
                'ञ', #0x91E, # DEVANAGARI LETTER NYA
                'ट', #0x91F, # DEVANAGARI LETTER TTA
                'ठ', #0x920, # DEVANAGARI LETTER TTHA
                'ड', #0x921, # DEVANAGARI LETTER DDA
                'ढ', #0x922, # DEVANAGARI LETTER DDHA
                'ण', #0x923, # DEVANAGARI LETTER NNA
                'त', #0x924, # DEVANAGARI LETTER TA
                'थ', #0x925, # DEVANAGARI LETTER THA
                'द', #0x926, # DEVANAGARI LETTER DA
                'ध', #0x927, # DEVANAGARI LETTER DHA
                'न', #0x928, # DEVANAGARI LETTER NA
                'प', #0x92A, # DEVANAGARI LETTER PA
                'फ', #0x92B, # DEVANAGARI LETTER PHA
                'ब', #0x92C, # DEVANAGARI LETTER BA
                'भ', #0x92D, # DEVANAGARI LETTER BHA
                'म', #0x92E, # DEVANAGARI LETTER MA
                'य', #0x92F, # DEVANAGARI LETTER YA
                'र', #0x930, # DEVANAGARI LETTER RA
                'ल', #0x932, # DEVANAGARI LETTER LA
                'ळ', #0x933, # DEVANAGARI LETTER LLA
                'व', #0x935, # DEVANAGARI LETTER VA
                'श', #0x936, # DEVANAGARI LETTER SHA
                'ष', #0x937, # DEVANAGARI LETTER SSA
                'स', #0x938, # DEVANAGARI LETTER SA
                'ह', #0x939, # DEVANAGARI LETTER HA
# Additional consonants
                'क़', #0x958, # DEVANAGARI LETTER QA ≡ 0x915 क 0x093C ◌़
                'ख़', #0x959, # DEVANAGARI LETTER KHHA ≡ 0x915 ख 0x093C ़
                'ग़', #0x95A, # DEVANAGARI LETTER GHHA ≡ 0x916 ग 0x093C ◌़
                'ज़', #0x95B, # DEVANAGARI LETTER ZA ≡ 0x91C ज 0x093C ़
                'ड़', #0x95C, # DEVANAGARI LETTER DDDHA ≡ 0x921 ड 0x093C ़
                'ढ़', #0x95D, # DEVANAGARI LETTER RHA ≡ 0x922 ढ 0x093C ◌़
                'फ़', #0x95E, # DEVANAGARI LETTER FA ≡ 0x92B फ 0x093C ◌़
                'य़', #0x95F, # DEVANAGARI LETTER YYA ≡ 0x92F य 0x093C ◌़
                'ऩ', #0x929, # DEVANAGARI LETTER NNNA • for transcribing Dravidian alveolar n ≡ 0x928 न  0x93C ◌़
                'ऱ', #0x931, # DEVANAGARI LETTER RRA • for transcribing Dravidian alveolar r • half form is represented as “Eyelash RA” ≡ 0x930 र  0x93C ◌़
                'ऴ', #0x934, # DEVANAGARI LETTER LLLA • for transcribing Dravidian l ≡ 0x933 ळ 0x93C ◌़
]

CONSONANTS_ADVANCED = [
# Additional consonants
                'ॸ', #0x978, # DEVANAGARI LETTER MARWARI DDA
                'ॹ', #0x979, # DEVANAGARI LETTER ZHA • used in transliteration of Avestan → 0xAF9 gujarati letter zha
                'ॺ', #0x97A, # DEVANAGARI LETTER HEAVY YA • used for an affricated glide JJYA
# Sindhi implosives
                'ॻ', #0x97B, # DEVANAGARI LETTER GGA
                'ॼ', #0x97C, # DEVANAGARI LETTER JJA
                'ॾ', #0x97E, # DEVANAGARI LETTER DDDA
                'ॿ', #0x97F, # DEVANAGARI LETTER BBA
]

DEPENDENT_VOWELS = [
                'ा', #0x93E, # DEVANAGARI VOWEL SIGN AA
                'ि', #0x93F, # DEVANAGARI VOWEL SIGN I • stands to the left of the consonant
                'ी', #0x940, # DEVANAGARI VOWEL SIGN II
                'ु', #0x941, # DEVANAGARI VOWEL SIGN U
                'ू', #0x942, # DEVANAGARI VOWEL SIGN UU
                'ृ', #0x943, # DEVANAGARI VOWEL SIGN VOCALIC R
                'ॄ', #0x944, # DEVANAGARI VOWEL SIGN VOCALIC RR
                'े', #0x947, # DEVANAGARI VOWEL SIGN E
                'ै', #0x948, # DEVANAGARI VOWEL SIGN AI
                'ो', #0x94B, # DEVANAGARI VOWEL SIGN O
                'ौ', #0x94C, # DEVANAGARI VOWEL SIGN AU
]
DEPENDENT_VOWELS_ADVANCED = [
                'ॉ', #0x949, # DEVANAGARI VOWEL SIGN CANDRA O
                'ॊ', #0x94A, # DEVANAGARI VOWEL SIGN SHORT O • Kashmiri, Bihari languages • also used for transcribing Dravidian short o
                'ॅ', #0x945, # DEVANAGARI VOWEL SIGN CANDRA E = candra
                'ॆ', #0x946, # DEVANAGARI VOWEL SIGN SHORT E • Kashmiri, Bihari languages • also used for transcribing Dravidian short e
                'ॎ', #0x94E, # DEVANAGARI VOWEL SIGN PRISHTHAMATRA E • character has historic use only • combines with E to form AI, with AA to form O,and with O to form AU
                'ॏ', #0x94F, # DEVANAGARI VOWEL SIGN AW • Kashmiri, Bihari languages
# These dependent vowel signs are used in Kashmiri and in the Bihari languages (Bhojpuri, Magadhi, and Maithili).
                'ऺ', #0x93A, # DEVANAGARI VOWEL SIGN OE
                'ऻ', #0x93B, # DEVANAGARI VOWEL SIGN OOE
                'ॕ', #0x955, # DEVANAGARI VOWEL SIGN CANDRA LONG E • used in transliteration of Avestan
# Dependent vowel signs for Kashmiri
                'ॖ', #0x956, # DEVANAGARI VOWEL SIGN UE
                'ॗ', #0x957, # DEVANAGARI VOWEL SIGN UUE
                'ॢ', #0x962, # DEVANAGARI VOWEL SIGN VOCALIC L
                'ॣ', #0x963, # DEVANAGARI VOWEL SIGN VOCALIC LL
]

MISC = [
# Various signs
                'ऽ', #0x93D, # DEVANAGARI SIGN AVAGRAHA
                'ॐ', #0x950, # DEVANAGARI OM → 1F549 🕉  om symbol
# Vedic tone marks
                '॑', #0x951, # DEVANAGARI STRESS SIGN UDATTA = Vedic tone svarita • mostly used for svarita, with rare use for udatta • used also in Vedic texts written in other scripts → 1CDA $᳚  vedic tone double svarita
                '॒', #0x952, # DEVANAGARI STRESS SIGN ANUDATTA = Vedic tone anudatta • used also in Vedic texts written in other scripts → 1CDC $᳜  vedic tone kathaka anudatta
# Accent marks
                '॓', #0x953, # DEVANAGARI GRAVE ACCENT → 0x300 $̀  combining grave accent
                '॔', #0x954, # DEVANAGARI ACUTE ACCENT → 0x301 $́  combining acute accent
# Generic punctuation for scripts of India These punctuation marks are for common use for the scripts of India despite being named "DEVANAGARI". They also occur as abbreviation signs in some South Indian scripts.
                '॥', #0x965, # DEVANAGARI DOUBLE DANDA = deergh viram 
# Glottal stop
                'ॽ', #0x97D # DEVANAGARI LETTER GLOTTAL STOP • used for writing Limbu in Devanagari • a glyph variant has the connecting top bar
]

DIGITS = [
                '०', #0x966, # DEVANAGARI DIGIT ZERO • also used to represent an anusvara following digits indicating secondary svara-s in Samavedic texts
                '१', #0x967, # DEVANAGARI DIGIT ONE
                '२', #0x968, # DEVANAGARI DIGIT TWO
                '३', #0x969, # DEVANAGARI DIGIT THREE
                '४', #0x96A, # DEVANAGARI DIGIT FOUR
                '५', #0x96B, # DEVANAGARI DIGIT FIVE
                '६', #0x96C, # DEVANAGARI DIGIT SIX
                '७', #0x96D, # DEVANAGARI DIGIT SEVEN
                '८', #0x96E, # DEVANAGARI DIGIT EIGHT
                '९', #0x96F, # DEVANAGARI DIGIT NINE
]
