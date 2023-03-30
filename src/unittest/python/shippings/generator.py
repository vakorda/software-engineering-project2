import pandas as pd

# sheet_name = 1 significa que coge los datos de la segunda hoja
df = pd.read_excel('G89.2023.T15.EG3.xlsx', sheet_name=1)

for index, row in df.iterrows():
    file_name = row['FILE PATH']
    file_content = row['FILE CONTENT']

    with open(file_name, 'w') as f:
        f.write(str(file_content))

#################################################

# Forma para crear algunos tests
def create_tests():
    # Numbers are inserted inbetween the elements of the array
    # take thing for the asser
    # sheet_name = 1 significa que coge los datos de la segunda hoja
    out = ""

    plantilla_1 = [
                    '    @freeze_time("2023-03-17")\n'
                    '    def test','(self):\n'
                    '        test_name = "test','.json"\n'
                    '        test_path = os.path.join(self.__test_folder, test_name)\n'
                    '\n'
                    '        with open(self.__shipping_path, "r", encoding="utf-8") as f:\n'
                    '            initial_shipings = json.load(f)\n'
                    '\n'
                    '        tracking_code = self.__order_manager.send_product(test_path)\n'
                    '        self.assertEqual("d1c866b1e6d8c1e9823c8bed8909dbbb2e96bc4a73e7687fa70c7ed7eee2d8cd", tracking_code)\n'
                    '\n'
                    '        with open(self.__shipping_path, "r", encoding="utf-8") as f:\n'
                    '            final_shipings = json.load(f)\n'
                    '\n'
                    '        self.assertNotEqual(initial_shipings, final_shipings)\n'
                    '\n'
                    '        valid_data = {\n'
                    '            "alg": "SHA-256",\n'
                    '            "typ": "DS",\n'
                    '            "tracking_code": "d1c866b1e6d8c1e9823c8bed8909dbbb2e96bc4a73e7687fa70c7ed7eee2d8cd",\n'
                    '            "order_id": "93ad8ecd0fc177ae373e3bbd3212b5c5",\n'
                    '            "issued_at": 1679011200.0,\n'
                    '            "delivery_day": 1679616000.0\n'
                    '            }\n'
                    '\n'
                    '        self.assertDictEqual(valid_data, final_shipings[-1])\n']
    plantilla_2 = [
                    '   @freeze_time("2023-03-17")\n'
                    '   def test', '(self):\n'
                    '        test_name = "test', '.json"\n'
                    '        test_path = os.path.join(self.__test_folder, test_name)\n'
                    '\n'
                    '        with open(self.__shipping_path, "r", encoding="utf-8") as f:\n'
                    '            initial_shipings = list(json.load(f))\n'
                    '\n'
                    '        with self.assertRaises(OrderManagementException) as ome:\n'
                    '            self.__order_manager.send_product(test_path)\n'
                    '        self.assertEqual("File provided not valid format", str(ome.exception))\n'
                    '\n'
                    '        with open(self.__shipping_path, "r", encoding="utf-8") as f:\n'
                    '            final_shipings = list(json.load(f))\n'
                    '\n'
                    '        self.assertListEqual(initial_shipings, final_shipings)\n']

    plantilla_3 = [
        '   @freeze_time("2023-03-17")\n'
        '   def test', '(self):\n'
        '        test_name = "test', '.json"\n'
        '        test_path = os.path.join(self.__test_folder, test_name)\n'
        '\n'
        '        with open(self.__shipping_path, "r", encoding="utf-8") as f:\n'
        '            initial_shipings = list(json.load(f))\n'
        '\n'
        '        with self.assertRaises(OrderManagementException) as ome:\n'
        '            self.__order_manager.send_product(test_path)\n'
        '        self.assertEqual("Input file incorrect format", str(ome.exception))\n'
        '\n'
        '        with open(self.__shipping_path, "r", encoding="utf-8") as f:\n'
        '            final_shipings = list(json.load(f))\n'
        '\n'
        '        self.assertListEqual(initial_shipings, final_shipings)\n']

    email_wrong_format = [
        '   @freeze_time("2023-03-17")\n'
        '   def test', '(self):\n'
        '        test_name = "test', '.json"\n'
        '        test_path = os.path.join(self.__test_folder, test_name)\n'
        '\n'
        '        with open(self.__shipping_path, "r", encoding="utf-8") as f:\n'
        '            initial_shipings = list(json.load(f))\n'
        '\n'
        '        with self.assertRaises(OrderManagementException) as ome:\n'
        '            self.__order_manager.send_product(test_path)\n'
        '        self.assertEqual("Delivery email wrong format", str(ome.exception))\n'
        '\n'
        '        with open(self.__shipping_path, "r", encoding="utf-8") as f:\n'
        '            final_shipings = list(json.load(f))\n'
        '\n'
        '        self.assertListEqual(initial_shipings, final_shipings)\n']

    order_id_wrong_format = [
        '   @freeze_time("2023-03-17")\n'
        '   def test', '(self):\n'
        '        test_name = "test', '.json"\n'
        '        test_path = os.path.join(self.__test_folder, test_name)\n'
        '\n'
        '        with open(self.__shipping_path, "r", encoding="utf-8") as f:\n'
        '            initial_shipings = list(json.load(f))\n'
        '\n'
        '        with self.assertRaises(OrderManagementException) as ome:\n'
        '            self.__order_manager.send_product(test_path)\n'
        '        self.assertEqual("Order id wrong format", str(ome.exception))\n'
        '\n'
        '        with open(self.__shipping_path, "r", encoding="utf-8") as f:\n'
        '            final_shipings = list(json.load(f))\n'
        '\n'
        '        self.assertListEqual(initial_shipings, final_shipings)\n']

    tests_con_plantilla2 = [2, 3, 5, 6, 7, 8, 9, 10, 11,
                            12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 31, 32, 33, 34, 35, 36, 37,
                            38, 39, 40, 41, 42, 43, 44, 45, 46,
                            47, 48, 49, 50, 51, 61, 62, 63, 64,
                            65, 66, 67, 68, 69, 70, 71, 72, 73]
    # Input file incorrect format
    tests_con_plantilla3 = [4, 23, 25, 52, 54, 74, 78]
    # Delivery email wrong format
    tests_email_wrong_format = [26, 27, 28, 29, 30, 55,57,59,79,80,81,82,83]
    # Order id wrong format
    tests_order_id_wrong_format = [24,53,75,76,77]

    other = [56,58]
    for i in other:
        out += plantilla_1[0]
        for j in range(len(plantilla_1) - 1):
            out += str(i)
            out += plantilla_1[j + 1]

    for i in tests_con_plantilla2:
        out += plantilla_2[0]
        for j in range(len(plantilla_2) - 1):
            out += str(i)
            out += plantilla_2[j + 1]

    for i in tests_con_plantilla3:
        out += plantilla_2[0]
        for j in range(len(plantilla_3) - 1):
            out += str(i)
            out += plantilla_3[j + 1]

    for i in tests_email_wrong_format:
        out += email_wrong_format[0]
        for j in range(len(email_wrong_format) - 1):
            out += str(i)
            out += email_wrong_format[j + 1]

    for i in tests_order_id_wrong_format:
        out += order_id_wrong_format[0]
        for j in range(len(order_id_wrong_format) - 1):
            out += str(i)
            out += order_id_wrong_format[j + 1]

    print(out)

create_tests()
