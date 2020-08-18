# Download dataset
shell('kaggle datasets download -d mdabbert/ultimate-ufc-dataset')

# Move downloaded file to project directory
shell('copy ultimate-ufc-dataset.zip C:\Personal\BIDAMIA_GoogleDrive\Business_Intelligence\R\Rmarkdown\ufc_fight_prediction\00_data\01_raw_data')
