Q1) Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listtlerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir.

def flatten(my_list):
    flat_list = []
    
    for element in my_list:
        if type(element) is list:
            for item in element:
                if type(item) is list:
                    for it in item:
                        if type(it) is list:
                            for new in it:
                                flat_list.append(new)
                            
                            
                        else:
                            flat_list.append(it)
                else:
                    flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list

Q2) Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün

def reverse_list(my_list):
    reverse_list = []
    
    for element in reversed(my_list):
        if type(element) is list:
            for item in reversed(element):
                if type(item) is list:
                    for it in reversed(item):
                        if type(it) is list:
                            for new in reversed(it):
                                reverse_list.append(new)
                            
                            
                        else:
                            reverse_list.append(it)
                else:
                    reverse_list.append(item)
        else:
            reverse_list.append(element)
    return reverse_list
