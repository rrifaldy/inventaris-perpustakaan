from flask import Flask, render_template, request, jsonify, make_response
import pymysql

# Membuat server flask
app = Flask(__name__)

mydb = pymysql.connect(
	host="localhost",
	user="root",
	passwd="afifsay",
	database="invertaris_perpus"
)

@app.route('/')
@app.route('/index')
def index():
    return render_template('dashboard.html')

@app.route('/get_barang_masuk', methods=['GET'])
def get_barang_masuk():
	query = "SELECT * FROM tb_barang_masuk WHERE 1=1"
	values = ()

	id_barang = request.args.get("id_barang_masuk")
	id_user = request.args.get("id_user")
	kode = request.args.get("kode_barang")
	nama = request.args.get("nama_barang")
	kategori = request.args.get("kategori")	
	jumlah = request.args.get("jumlah")
	date = request.args.get("datetime")

	if id_barang:
		query += " AND id_barang_masuk=%s "
		values += (id_barang,)
	if id_user:
		query += " AND id_user=%s "
		values += (id_user,)
	if kode:
		query += " AND kode_barang=%s "
		values += (kode,)
	if nama:
		query += " AND nama_barang LIKE %s "
		values += ("%"+nama+"%", )
	if kategori:
		query += " AND kategori=%s "
		values += (kategori,)
	if jumlah:
		query += " AND jumlah=%s "
		values += (jumlah,)
	if date:
		query += " AND datetime=%s "
		values += (date,)

	mycursor = mydb.cursor()
	mycursor.execute(query, values)
	data = mycursor.fetchall()
	row_headers = [x[0] for x in mycursor.description]
	json_data = []
	for result in data:
		json_data.append(dict(zip(row_headers, result)))

	return make_response(jsonify(json_data),200)

@app.route('/insert_barang_masuk', methods=['POST'])
def insert_barang_masuk():
	hasil = {"status": "gagal insert data barang masuk"}

	try:
		data = request.json

		query = "INSERT INTO tb_barang_masuk(id_barang_masuk, id_user, kode_barang, nama_barang, kategori, jumlah, datetime) VALUES(%s,%s,%s,%s,%s,%s,%s)"
		values = (data["id_barang_masuk"],data["id_user"], data["kode_barang"],data["nama_barang"], data["kategori"], data["jumlah"])
		mycursor = mydb.cursor()
		mycursor.execute(query, values)
		mydb.commit()
		hasil = {"status": "berhasil insert data barang masuk"}

	except Exception as e:
		print("Error: " + str(e))

	return jsonify(hasil)

# Belum Jadi
@app.route('/update_barang_masuk', methods=['PUT'])
def update_barang_masuk():
	hasil = {"status": "gagal update data barang masuk"}

	try:
		data = request.json
		id_masuk_awal = data["id_masuk_awal"]

		query = "UPDATE tb_barang_masuk SET id_barang_masuk = %s "
		values = (id_masuk_awal, )

		if "id_masuk_ubah" in data:
			query += ", id_barang_masuk = %s"
			values += (data["id_masuk_ubah"], )
		if "id_user" in data:
			query += ", id_user = %s"
			values += (data["id_user"], )
		if "kode" in data:
			query += ", kode_barang = %s"
			values += (data["kode"], )
		if "nama" in data:
			query += ", nama_barang = %s"
			values += (data["nama"], )
		if "kategori" in data:
			query += ", kategori = %s"
			values += (data["kategori"], )
		if "jumlah" in data:
			query += ", jumlah = %s"
			values += (data["jumlah"], )
		if "date" in data:
			query += ", datetime = %s"
			values += (data["date"], )
			

		query += " WHERE nis = %s"
		values += (id_masuk_awal, )

		mycursor = mydb.cursor()
		mycursor.execute(query, values)
		mydb.commit()
		hasil = {"status": "berhasil update data barang masuk"}

	except Exception as e:
		print("Error: " + str(e))

	return jsonify(hasil)

@app.route('/delete_barang_masuk/<id_barang_masuk>', methods=['DELETE'])
def delete_barang_masuk(id_barang_masuk):
	hasil = {"status": "gagal hapus data barang masuk"}

	try:
		query = "DELETE FROM tb_barang_masuk WHERE id_barang_masuk=%s"
		values = (id_barang_masuk,)
		mycursor = mydb.cursor()
		mycursor.execute(query, values)
		mydb.commit()
		hasil = {"status": "berhasil hapus data barang masuk"}

	except Exception as e:
		print("Error: " + str(e))

	return jsonify(hasil)


@app.route('/get_barang_keluar', methods=['GET'])
def get_barang_keluar():
	query = "SELECT * FROM tb_barang_keluar WHERE 1=1"
	values = ()

	id_barang = request.args.get("id_barang_keluar")
	id_user = request.args.get("id_user")
	kode = request.args.get("kode_barang")
	nama = request.args.get("nama_barang")
	kategori = request.args.get("kategori")	
	jumlah = request.args.get("jumlah")
	date = request.args.get("datetime")

	if id_barang:
		query += " AND id_barang_keluar=%s "
		values += (id_barang,)
	if id_user:
		query += " AND id_user=%s "
		values += (id_user,)
	if kode:
		query += " AND kode_barang=%s "
		values += (kode,)
	if nama:
		query += " AND nama_barang LIKE %s "
		values += ("%"+nama+"%", )
	if kategori:
		query += " AND kategori=%s "
		values += (kategori,)
	if jumlah:
		query += " AND jumlah=%s "
		values += (jumlah,)
	if date:
		query += " AND datetime=%s "
		values += (date,)

	mycursor = mydb.cursor()
	mycursor.execute(query, values)
	data = mycursor.fetchall()
	row_headers = [x[0] for x in mycursor.description]
	json_data = []
	for result in data:
		json_data.append(dict(zip(row_headers, result)))

	return make_response(jsonify(json_data),200)

@app.route('/delete_barang_keluar/<id_barang_keluar>', methods=['DELETE'])
def delete_barang_keluar(id_barang_keluar):
	hasil = {"status": "gagal hapus data barang masuk"}

	try:
		query = "DELETE FROM tb_barang_keluar WHERE id_barang_keluar=%s"
		values = (id_barang_keluar,)
		mycursor = mydb.cursor()
		mycursor.execute(query, values)
		mydb.commit()
		hasil = {"status": "berhasil hapus data barang Keluar"}

	except Exception as e:
		print("Error: " + str(e))

	return jsonify(hasil)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5010, debug=True)
