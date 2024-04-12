import streamlit as st
import joblib
import pandas as pd
import numpy as np
import time

PAGE_TITLE = "Banglore House Price Prediction | Machine Larning"
PAGE_ICON = "🏠"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.sidebar.markdown(" ### Navigation Bar")


model = joblib.load("CV/house/model.joblib")
encoder = joblib.load("CV/house/encoder.joblib")

st.title("House Price Prediction")

st.image("CV/house/img.jpg",use_column_width=True)


st.markdown("## Download the template")
st.write("Please download the template file and fill it up with all the required data, and please make sure not to leave any column empty")
st.write("If one or more than one column/columns is/are left empty you will be displayed a list of all the empty columns, please use the list as a reference to fill up all of your empty columns ")

file ="CV/house/sample.csv"
data = pd.read_csv(file)
st.download_button(
    label='Download the Template', 
    data=data.to_csv(index=False), 
    file_name='data.csv', 
    mime='text/csv'
    )

st.write("You can refer to this text document to get all the information regarding the columns and fill the columns with the relevant data accordingly")

file_path = "CV/house/data_description.txt"
with open(file_path, 'r') as file:
    data = file.readlines()
st.write("Data description:")
st.download_button(label='Download the data description', data='\n'.join(data), file_name='data.txt', mime='text/plain')

st.write("Once you have read the 'data.txt' and understood all the columns and their values download the 'template.csv' and fill up all the columns.")
st.write("Each row will contain the data of a house , the no of rows depend on the number of house you want to predict the value of.")

csv_file = st.file_uploader("Upload the file in CSV fromat",type=['csv'])
if csv_file is not None:
    test = pd.read_csv(csv_file)
    st.write(test)


if st.button("Submit"):
    
    # Attempting to fill some of the null values
    
    test['LotFrontage']=test['LotFrontage'].fillna(test['LotFrontage'].mean())
    test['MSZoning']=test['MSZoning'].fillna(test['MSZoning'].mode()[0])
    test['Utilities']=test['Utilities'].fillna(test['Utilities'].mode()[0])
    test['Alley']=test['Alley'].fillna('none')
    test['SaleType']=test['SaleType'].fillna('Oth')
    test['Exterior1st']=test['Exterior1st'].fillna(test['Exterior1st'].mode()[0])
    test['Exterior2nd']=test['Exterior2nd'].fillna(test['Exterior2nd'].mode()[0]) 
    test['BsmtFinSF1']=test['BsmtFinSF1'].fillna(test['BsmtFinSF1'].mode()[0])    
    test['BsmtFinSF2']=test['BsmtFinSF2'].fillna(test['BsmtFinSF2'].mode()[0])
    test['BsmtUnfSF']=test['BsmtUnfSF'].fillna(test['BsmtUnfSF'].mode()[0])
    test['TotalBsmtSF']=test['TotalBsmtSF'].fillna(test['TotalBsmtSF'].mode()[0])
    test['BsmtFullBath']=test['BsmtFullBath'].fillna(test['BsmtFullBath'].mode()[0])
    test['BsmtHalfBath']=test['BsmtHalfBath'].fillna(test['BsmtHalfBath'].mode()[0])
    test['KitchenQual']=test['KitchenQual'].fillna(test['KitchenQual'].mode()[0])
    test['Functional']=test['Functional'].fillna(test['Functional'].mode()[0])
    test['GarageCars']=test['GarageCars'].fillna(test['GarageCars'].mode()[0])    
    test['MasVnrType']=test['MasVnrType'].fillna('None')
    test['MasVnrArea']=test['MasVnrArea'].fillna(test['MasVnrArea'].mode()[0])
    test['GarageArea']=test['GarageArea'].fillna(test['GarageArea'].mode()[0])    
    test['BsmtQual']=test['BsmtQual'].fillna('No Basement')
    test['BsmtCond']=test['BsmtCond'].fillna('No Basement')
    test['BsmtExposure']=test['BsmtExposure'].fillna('No Basement')
    test['BsmtFinType1']=test['BsmtFinType1'].fillna('No Basement')
    test['BsmtFinType2']=test['BsmtFinType2'].fillna('No Basement')
    test['Electrical']=test['Electrical'].fillna(test['Electrical'].mode()[0])
    test['GarageType']=test['GarageType'].fillna('No Garage')
    test['GarageQual']=test['GarageQual'].fillna('No Garage')
    test['GarageCond']=test['GarageCond'].fillna('No Garage')
    test['FireplaceQu']=test['FireplaceQu'].fillna('No Fireplace')    
    test['PoolQC']=test['PoolQC'].fillna('None')    
    test['Fence']=test['Fence'].fillna('None')    
    test['MiscFeature']=test['MiscFeature'].fillna('None')
    
    # Displaying all the columns that have null value
    null_mask = test.isnull().any()
    columns_with_null = test.columns[null_mask]
    st.write("Columns with null values are:")
    st.write(columns_with_null)
    
    # Encoding the columns
    object_col = test.select_dtypes(include=['object'])
    cols = object_col.columns
    new_test = test
    encoded_cols_test = encoder.transform(object_col)
    encoded_df_test = pd.DataFrame(encoded_cols_test, columns=encoder.get_feature_names_out(cols))
    new_test = new_test.drop(columns=cols)
    encoded_data_test = pd.concat([new_test, encoded_df_test], axis=1)
    
    # Predicting the data
    test_pred = model.predict(encoded_data_test)
    output = pd.DataFrame({'Id': test.Id, 'SalePrice': test_pred})
    st.write("Your Prediction is ready")
    progress = st.progress(0)
    for i in range (100):
        time.sleep(0.01)
        progress.progress(i+1)
    st.write(output)
    st.download_button(
        label='Download your predictions', 
        data=output.to_csv(index=False), 
        file_name='output.csv', 
        mime='text/csv')



        
        
