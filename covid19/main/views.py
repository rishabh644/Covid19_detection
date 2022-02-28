from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import models
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
# Create your views here.
def index(request):
        template=loader.get_template('main/mainfolder/contact-form-13/index.html')
        context={}
        return HttpResponse(template.render(context,request))
def cal(request):
        template=loader.get_template('main/positive/ContactFrom_v2/index.html')
        template1=loader.get_template('main/negative/ContactFrom_v11/index.html')
        context={}
        files=request.FILES #multivalued dict
        picture=files.get("xray")
        instance=models.ImageModel()
        instance.image=picture
        instance.save()
        username=request.POST.get('name')
        dob=request.POST.get('dob')
        address=request.POST.get('address')
        print('Name ',username)
        print('Dob ',dob)
        context={'name':username,'dob':dob,'address':address}
        mdl=load_model('C:/Users/hp/OneDrive/Desktop/minorproject/covid19/main/TrainedModel.h5')
        img_width,img_height=224,224
        mdl.compile(loss='binary_crossentropy',optimizer='rmsprop',metrics=['accuracy'])
        ptt='C:/Users/hp/OneDrive/Desktop/minorproject/covid19/media/'
        ptt+=instance.fx()
        img=image.load_img(ptt,target_size=(img_width,img_height))
        x=image.img_to_array(img)
        x=np.expand_dims(x,axis=0)
        images=np.vstack([x])
        predict_x=(mdl.predict(images) > 0.5).astype("int32")
        if(predict_x[0][0]==0):
                return HttpResponse(template.render(context,request))
        else:
                return HttpResponse(template1.render(context,request))
        
        
        
        
        
        

        
       

