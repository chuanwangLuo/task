import csv
from app import db  
from app import Country, Series, Record  

def import_data_from_csv(csv_file_path):
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            country_name = row['Country Name']
            country_code = row['Country Code']
            series_name = row['Series Name']
            series_code = row['Series Code']
            try:
                year2021 = None if row['2021 [YR2021]'] in ('..', '') else float(row['2021 [YR2021]'])
                year2022 = None if row['2022 [YR2022]'] in ('..', '') else float(row['2022 [YR2022]'])
            except ValueError as e:
                print(f"Error converting year data for {country_name} - {series_name}: {e}")
                year2021 = None
                year2022 = None
            
            
            country = Country.query.filter_by(code=country_code).first()
            if not country:
                country = Country(name=country_name, code=country_code)
                db.session.add(country)
            
            
            series = Series.query.filter_by(code=series_code).first()
            if not series:
                series = Series(name=series_name, code=series_code)
                db.session.add(series)
            
            
            record = Record(country=country, series=series, year2021=year2021, year2022=year2022)
            db.session.add(record)
        
        
        db.session.commit()

if __name__ == "__main__":
    import_data_from_csv('data.csv')  
