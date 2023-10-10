result = [
    'sensor_03_data: c8050eed40ef171cc2784d638b34fa781359331a3ed13a32e97cc31667ba',
    'sensor_01_data: a043bae1603803a839c0cb52f511d9cb8f68d9d9b0341314a5534ea92b26',
    'sensor_05_data: 3b36a45c17ff134eee52db9fa0d4af211849b3a47ed1640ca4b8601ee8d9',
]


result.sort(key=lambda r: int(r.split("_")[1]))
print(result)
