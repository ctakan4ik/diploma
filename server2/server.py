import socket
import create_db
from datetime import datetime
import parser_data
import analyze
import recommend

while True:
    sock = socket.socket()
    sock.bind( ('192.168.0.104', 8080) )
    sock.listen(1)
    print('waiting for connection...')
    conn, addr = sock.accept()
    print('connected: ', addr)
    data = conn.recv(1024)
    city = data.decode("utf-8")
    action = city[:1]
    city = city[1:]
    print(type(city))
    date = datetime.now().date()
    date = str(date)
    city_id = create_db.city_find(city)
    city_id = int(city_id[0])
    if action == '2':
        if create_db.cases_check(date, city_id):
            cases = create_db.cases_check(date, city_id)
            cases = str(cases)
            cases = 'Количество заболевших в городе:' + cases
            conn.send(cases.encode("utf-8"))
            conn.close()
            print('эт1')
        else:
            link = parser_data.get_link(city)
            html = parser_data.get_data(link)
            data, cases = parser_data.clear_data(html)
            create_db.cases_in(date, cases[6], city_id)
            rec_data = analyze.analyze(cases)
            create_db.recomm_in(date, rec_data, city_id)
            cases = create_db.cases_check(date, city_id)
            cases = str(cases)
            cases = 'Количество заболевших в городе:' + cases
            conn.send(cases.encode("utf-8"))
            conn.close()
            print('эт2')
    elif action == '1':
        if create_db.cases_check(date, city_id):
            cases = create_db.cases_check(date, city_id)
            recom_data = create_db.rec_check(date,city_id)
            cases = recommend.casesPerThousand(cases,city)
            result = recommend.recommend(cases,recom_data)
            conn.send(result.encode("utf-8"))
            conn.close()
            print('эт3')
        else:
            link = parser_data.get_link(city)
            html = parser_data.get_data(link)
            data, cases = parser_data.clear_data(html)
            create_db.cases_in(date, cases[6], city_id)
            rec_data = analyze.analyze(cases)
            create_db.recomm_in(date, rec_data, city_id)
            cases = create_db.cases_check(date, city_id)
            cases = recommend.casesPerThousand(cases,city)
            result = recommend.recommend(cases, rec_data)
            conn.send(result.encode("utf-8"))
            conn.close()
            print('эт4')
