import csv
from pytorch_prototype import prototype

class plant_prediction:
    def __init__(self, img_name):
        self.img_name = img_name

    def read_labels(self):
        mydict = {}
        with open('labels.csv', mode='r') as infile:
            reader = csv.reader(infile)
            with open('labels_new.csv', mode='w') as outfile:
                writer = csv.writer(outfile)
                mydict = {rows[0]: rows[1] for rows in reader}
        return mydict

    def predict_label(self):
        ptf = prototype(verbose=1)
        ptf.Prototype("plant_disease", "exp3", eval_infer=True)
        predictions = ptf.Infer(img_name=self.img_name, return_raw=True)
        pred_class = predictions['predicted_class']
        label_dict = self.read_labels()
        out_label = label_dict[pred_class]
        return out_label

    """def final_output(self):
        return self.predict_label(self.predictions)"""


#planted = plant_prediction()
#o_l=planted.predict_label()



