import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('./data.csv')
  country_name = input('Type Country => ')

  result = utils.population_by_country(data, country_name)

  if len(result) > 0:
    country = result[0]
    keys, values = utils.get_population(country)
    charts.generate_bar_chart(country_name,keys, values)
    charts.generate_pie_chart(keys, values)

if __name__ == '__main__':
  run()