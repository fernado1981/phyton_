from API.GetPrueba.Searchdata import Searchdata


class ApiPrueba:
     #dada una url
     url = "http://demo5977139.mockable.io/qa-cdco/exercises/cars_02"
     #dado el datgo a buscar
     data = 'parkings'
     #cereamos un objeti de tipo SearchData y le pasamos la url y el data al constructor
     search = Searchdata(url, data)
     #invocamos el método searchApiGet de SeachData
     search.searchApiGet()
