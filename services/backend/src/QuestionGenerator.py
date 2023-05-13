from src.QMaker import main as qm
class QGenerator:
    def __init__(self, text):
        self.input_text = {
            "input_text": text
        }
    
    def gerateMCQ(self):
        qg = qm.QGen()
        print(self.input_text)
        output = qg.predict_mcq(self.input_text)
        results = dict()
        for i in range(len(output["questions"])):
            results[i] = {"question": output["questions"][i]["question_statement"], 
                       "answer": output["questions"][i]["answer"],
                       "options": output["questions"][i]["options"]}
        return results


            