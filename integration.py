from re import T
import skimage.io as io
from utilities import getSymboles
from utilities import predict
from utilities import classification_mapping
from utilities import grouping
from utilities import ApplyOnImage



def OverLapping(path,modelPath):

    image = io.imread(path,as_gray=True)

    # io.imshow(image) 
    # io.show()
    symbolesList = getSymboles(image)
    features = []
    for symbol in symbolesList:
        io.imshow(symbol[0]) 
        io.show()
        prediction = predict(symbol[0],modelPath)
        prediction = classification_mapping(prediction)
        features.append((prediction, symbol[1], symbol[2]))
    cards = grouping(features)
    print("Cards are:", cards)
    print("Total Number of Cards:", len(cards))

def NonOverLapping(path,modelPath):

    image = io.imread(path)

    splitedCorners=ApplyOnImage(image)

    cards=[]

    for corner in splitedCorners:
        # io.imshow(corner[0]/255.0) 
        # io.show()
        # io.imshow(corner[1]/255.0) 
        # io.show()
        p1=predict(corner[0]/255.0,modelPath)
        p2=predict(corner[1]/255.0,modelPath)

        p1=classification_mapping(p1)
        p2=classification_mapping(p2)
        cards.append((p1,p2))

    print("Cards are:", cards)
    print("Total Number of Cards:", len(cards))


def main():

    path="Grouping/AcetoFive.jpeg"
    modelPath="Model/SVC_model.joblib"
    AlgoNum=0

    if(AlgoNum==0 or AlgoNum==2):
        OverLapping(path,modelPath)
    if(AlgoNum==1 or AlgoNum==2):
        NonOverLapping(path,modelPath)



if __name__ == "__main__":
    main()

    try:
        pass

    except:
        print("Sea7k trb")
