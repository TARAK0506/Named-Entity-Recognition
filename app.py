from imports import *

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST':

        data=CustomData(input_file=request.files['input_file'])
        file_extension=data.save_data()
        print(file_extension)


    # return render_template()


if __name__=="__main_":
    app.run(host="0.0.0.0",debug=True)