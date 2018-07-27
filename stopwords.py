hi_stopwords = set(['इन', 'परंतु', 'हुआ', 'सो', 'दवारा', 'भीतर', 'है', 'वहाँ', 'और', 'थे', 'एसे', 'भितर', 'कहते', 'यहाँ', 'गये', 'गयी', 'सभी', 
                    'लिया', 'उसे', 'कहा', 'जिन', 'उसी', 'बनी', 'स्थान', 'रवासा', 'बही', 'होता', 'मै', 'रहा', 'हुये', 'दबारा', 'आदि', 'कितना',
                    'कुल', 'जब', 'तिन', 'तिन्हें', 'किस', 'नहिं', 'करता', 'बाद', 'होति', 'कल', 'हें', 'उन', 'अपनि', 'जो', 'जैसा', 'साभ',
                    'अप', 'नहीं', 'मध्य', 'इत्यादि', 'इसका', 'जिन्हें', 'पूरे', 'दोनों', 'इंहें', 'ऱ्वासा', 'जेसा', 'उच्च', 'गई', 'उन्हें', 'था', 'निहायत',
                    'पहले', 'जिससे', 'जैसे', 'अभी', 'अभि', 'कभी', 'नीचे', 'तिंहें', 'रहे', 'दुसरे', 'कोन', 'संग', 'जहां', 'इसे', 'हुए', 'हैं',
                    'जहाँ', 'किन्हों', 'उनकि', 'अपना', 'मानो', 'ये', 'लिए', 'तिस', 'किया', 'इन्हीं', 'जिधर', 'तरह', 'बाला', 'उनकी', 'इंहिं', 
                    'गया', 'हुई', 'सकता', 'समय', 'इन्हों', 'ऊपर', 'कम', 'किंहों', 'उन्हीं', 'इनके', 'इंहों', 'दिया', 'इन्हें', 'बिलकुल', 'ऐसा', 
                    'आप', 'तो','साथ', 'में', 'किसि', 'ने', 'लेकिन', 'कोइ', 'होने', 'उंहों', 'की', 'से', 'बहुत', 'हो', 'दूर', 'जिन्हों', 'तक',
                    'किर', 'कुछ', 'जेसे', 'इसमें', 'हुअ', 'जाता', 'तिन्हों', 'जिस', 'अन्य', 'कौनसा', 'करते', 'एवं', 'ही', 'पुरा', 'लेकर',
                    'जिसमें', 'थी', 'अत', 'इसकी', 'वर्ग', 'होना', 'होती', 'ऐसे', 'कोनसा','बड़े', 'थि', 'दूसरे', 'रहती', 'ओर', 'इनका',
                    'वगेरह', 'काफि', 'अथवा', 'वहिं', 'इसके', 'अपने', 'हे', 'जितना', 'भी', 'बाहर', 'वह', 'जा', 'ना', 'कौन', 'कर', 
                    'यही', 'उनको', 'सारा', 'करना', 'पे', 'व', 'हि', 'इस', 'कोई', 'कई', 'आज', 'सबसे', 'रखें', 'इसकि', 'तुम', 'कइ',
                    'यिह', 'किंहें', 'दुसरा', 'वहां', 'वुह', 'बहि', 'करने', 'यहां', 'लिये', 'जाते', 'उन्हों', 'वग़ैरह', 'उस', 'एक', 'फिर', 'गए',
                    'कि', 'उसि', 'जिंहों', 'वरग', 'यहि', 'अपनी', 'इसी', 'वे', 'वहीं', 'सकते', 'हुइ', 'अब', 'किए', 'जिसे', 'का', 'किसे',
                    'सकती', 'किन्हें', 'मगर', 'जिंहें', 'इतयादि', 'द्वारा', 'बड़ा', 'उनके', 'न', 'प्रति', 'दो', 'पर', 'काफ़ी', 'बनि', 'तब', 
                    'तिसे', 'बीच', 'उसके', 'एस', 'पूरा', 'अदि', 'सभि', 'उंहें', 'उनका', 'तथा', 'उसकी', 'यदि','साबुत', 'किसी', 'के', 
                    'अंदर', 'घर', 'उंहिं', 'होते', 'निचे', 'जाने', 'करें', 'उत्तर', 'जीधर', 'भि', 'जाती', 'इसि', 'यह', 'मे', 'को', 'वाले', 
                    'तिंहों', 'या'])
en_stopwords = set(['him', 'itself', 'somewhere', 'with', 'become', 'ie', 'because', 'his', 'therein', 'these', 'whenever', 
                    'side', 'no', 'four', 'even', 'from', 'find', 's', 'always', 'system', 'together', 'using', 'several', 
                    "mightn't", 'seeming', 'cant', 't', 'elsewhere', 'whose', 'toward', 'third', 'call', "mustn't", 
                    'hasnt', 'interest', 'those', 'couldn', 'well', 'a', 'next', 'such', 'seemed', 'except', 'de', 'thick',
                    'perhaps', 'anything', 'already', 'why', 'yourselves', 'behind', 'hundred', 'some', 'for', 'hence',
                    'herein', 'this', 'forty', 'became', 'other', 'your', 'seem', 'detail', 'its', "weren't", 'see', 'across',
                    'cannot', 'also', 'otherwise', 'nowhere', 'km', 'inc', 'aren', 'quite', 'wouldn', 'serious', "needn't",
                    'shouldn', 'again', 'bottom', 'thence', 'becoming', 'and', 'yourself', 'or', 'anyway', 'might', 'through',
                    'down', 'whereupon', 'throughout', 'less', 'whole', 'you', 'thru', 'under', 'many', 'keep', 'anywhere', 
                    'indeed', "you're", 'per', 'who', 'ours', 'do', 'won', 'to', 'describe', 'however', 'namely', 'empty', 
                    'top', 'nine', "wouldn't", 'none', 'that', 'bill', 'mustn', 'below', 'others', 'another', "wasn't", 
                    'moreover', 'at', 'may', 'myself', 'can', 'sometimes', 'almost', "it's", 'would', 'hasn', 'unless', 
                    'don', 'whatever', 'whence', 'hadn', 'anyone', "isn't", 'now', 'so', "hadn't", 'go', 'noone', 'all', 
                    'were', 'although', 'etc', 'alone', 'our', 'whereby', 'been', 'where', 'within', 'everywhere', 'theirs',
                    'beforehand', 'co', 'there', 'afterwards', 'rather', 'each', 'three', 'over', "didn't", 'whither', 
                    'fifteen', 'out', 'how', 'if', 'never', 'could', 'fire', 'mill', 'five', 'himself', 'done', 'couldnt', 
                    'was', 'when', 'only', 'either', 'whether', 'she', 'it', 'latter', 'have', "she's", "should've", 'amongst',
                    'eg', "aren't", "don't", 'due', 'an', 'most', 'shan', "shan't", 'much', 'into', 'i', 'nothing', 'y', 
                    'whereafter', 'something', 'since', 'which', 'here', 'are', 'two', "you'll", 'upon', 'various', 
                    'hereafter', 'my', 'hereupon', 'me', 'somehow', 'show', 'though', 'between', 'eight', 'sometime', 
                    'thereby', 'by', 'part', 'someone', 'meanwhile', 'having', 'during', 've', 'name', 'con', 'once', 
                    'o', 'on', 'doing', 'along', 'else', 'therefore', 'be', 'but', 'he', 'than', 'ever', 'should', 'mine',
                    'formerly', 'what', "you'd", 'themselves', 'nor', 'put', 'did', 'will', 'eleven', 'nevertheless', 
                    'give', 'wherever', "shouldn't", 'whereas', 'nobody', 'after', 'does', 'thus', 'kg', 'll', 'hers', 
                    'front', 'full', 'least', 'thin', 'besides', 'ltd', 'six', 'neither', 'among', 'cry', 'twelve',
                    'regarding', 'us', "haven't", "you've", 'becomes', 'more', 'beside', 'made', 'sixty', 'same', 'isn', 
                    'around', 'get', 'seems', 'needn', 'really', 'enough', 'latterly', "that'll", 'yours', 'weren', 'too',
                    'former', 'un', "doesn't", 'her', 'yet', 'found', 'one', 'haven', 'very', 'please', 'without', 'wasn',
                    'ain', 'any', 'of', 'twenty', 'make', 'as', 'doesn', 'every', 'while', 're', 'fill', 'above', 'own', 
                    'off', 'both', 'take', 'amoungst', 'didn', 'back', 'their', "hasn't", 'often', 'sincere', 'computer',
                    'further', 'ten', 'onto', 'just', 'beyond', 'about', 'against', 'whoever', 'we', 'used', 'thereupon',
                    'anyhow', 'hereby', 'everyone', 'them', 'amount', 'must', 'first', 'up', "couldn't", 'move', 'before',
                    'still', 'few', 'whom', 'fify', 'm', "won't", 'ourselves', 'via', 'had', 'being', 'thereafter', 'they',
                    'mostly', 'in', 'herself', 'towards', 'last', 'am', 'is', 'wherein', 'until', 'everything', 'mightn', 
                    'not', 'say', 'ma', 'has', 'then', 'd', 'the'])
