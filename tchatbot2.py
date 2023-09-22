# On classe des mots clefs dans des intentions (tokenization)
# brain pretrain to multi layers classification
patterns = {
    "access": ["access","lost","account","where"],
    "expiry": ["limited","timeframe","expires","expiry","expire","limit","time"],
    "release": ["when", "release","month","date","day","released"],
    "revisited": ["live","revisited","revisit","visit","rewatch"],
    "greeting": ["hi","hey","help","hello","how are you"],
}

class IntentClassifier(object):
    def __init__(self, patterns):
        self.patterns = patterns

    def classify(self, text):
        for intent, pattern in self.patterns.items():
            for word in pattern:
                if word in text.lower():
                    return intent
        return "greeting"

intent_classifer = IntentClassifier(patterns)
classification = intent_classifer.classify("How are you today ?")

answers = {
    "greeting": "Hello. Please ask me a question.",
    "access": "We provide our courses online via our training site.",
    "expiry": "Our courses have no expiration date or add-on fees.",
    "release": "We expect to release this masterclass by may.",
    "revisited": "The masterclass can be revisited."
}

class AnswerGenerator(object):

    def __init__(self, patterns):
        self.answers = patterns

    def generateAnswer(self, intent):
        if intent in self.answers:
            return self.answers[intent]
        return self.answers["greeting"]

answer_generator = AnswerGenerator(answers)

N_ANSWERS = 5
for i in range(0,N_ANSWERS):
    u_input = input()
    intent = intent_classifer.classify(u_input)
    answer = answer_generator.generateAnswer(intent)
    print(answer)
