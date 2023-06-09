from django import forms
from shop.models import Product
from category.models import Category, Sub_Category
from accounts.models import Account
from orders.models import Coupon
import datetime


class loginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control mb-3 mt-1 validate',}), max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mt-1  validate',}), label="Password")
    

class productForm(forms.ModelForm):
    class Meta:
         model = Product
         fields = ['product_name', 'slug', 'description', 'price', 'unit', 'image_1', 'image_2', 'image_3', 'image_4', 'stock',
                      'is_available', 'is_featured', 'category', 'sub_category']
        
    def __init__(self, *args, **kwargs):
        super(productForm,self).__init__(*args, **kwargs)
        self.fields['price'].widget.attrs['min'] = 0
        self.fields['stock'].widget.attrs['min'] = 0
        for field  in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['is_available'].widget.attrs['type'] = 'checkbox'
        self.fields['is_featured'].widget.attrs['type'] = 'checkbox'
        self.fields['is_available'].widget.attrs['class'] = 'form-check-input'
        self.fields['is_featured'].widget.attrs['class'] = 'form-check-input'
                
class categoryForm(forms.ModelForm):
    class Meta:
         model = Category
         fields = ['category_name', 'slug','description', 'category_image',]
        
    def __init__(self, *args, **kwargs):
        super(categoryForm,self).__init__(*args, **kwargs)
        for field  in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            
            
class subCategoryForm(forms.ModelForm):
    class Meta:
         model = Sub_Category
         fields = ['sub_category_name', 'slug', 'description', 'category', 'is_featured',]
         
    def __init__(self, *args, **kwargs):
        super(subCategoryForm,self).__init__(*args, **kwargs)
        for field  in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['is_featured'].widget.attrs['type'] = 'checkbox'
        self.fields['is_featured'].widget.attrs['class'] = 'form-check-input'


class userForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'is_admin', 'is_staff', 'is_superadmin','is_active']
        
    def __init__(self, *args, **kwargs):
        super(userForm,self).__init__(*args, **kwargs)
        self.fields['phone_number'].widget.attrs['maxlength'] = 10
        
        for field  in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['is_admin'].widget.attrs['class'] = 'form-check-input'
        self.fields['is_active'].widget.attrs['class'] = 'form-check-input'
        self.fields['is_staff'].widget.attrs['class'] = 'form-check-input'
        self.fields['is_superadmin'].widget.attrs['class'] = 'form-check-input'
        self.fields['is_admin'].widget.attrs['type'] = 'checkbox'
        self.fields['is_active'].widget.attrs['type'] = 'checkbox'
        self.fields['is_staff'].widget.attrs['type'] = 'checkbox'
        self.fields['is_superadmin'].widget.attrs['type'] = 'checkbox'


class dateInput(forms.DateInput):
    input_type = 'date'


class couponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = ['code', 'discount','min_value','valid_at','active']
        widgets = {
                    'valid_at': dateInput(),
                    }
    def __init__(self, *args, **kwargs):
        super(couponForm,self).__init__(*args, **kwargs)
        self.fields['valid_at'].widget.attrs['min'] = str(datetime.date.today())
        self.fields['active'].widget.attrs['type'] = 'checkbox'
        for field  in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['active'].widget.attrs['class'] = 'form-check-input'