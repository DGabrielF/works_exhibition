import re

class Validating:
    def matchTest(parameter, regex, is_nome):
        if is_nome:
            recompile = re.compile(regex, re.IGNORECASE)
        else:
            recompile = re.compile(regex)
        # print(P)
        if recompile.match(parameter):
            return True
        else:
            return False

    def integer(parameter, len_entry, can_be_negative=False):
        is_nome = False
        if can_be_negative is True:
            if len_entry is None:
                regex = r"(\-{0,1})(^\d*$)"
            elif type(len_entry) is int:
                regex = r"(\-{0,1})(^\d{0,"+f'{len_entry}'+r"}$)"
            else:
                regex = r"(\-{0,1})(^$)"
        else:
            if len_entry is None:
                regex = r"(^\d*$)"
            elif type(len_entry) is int:
                regex = r"(^\d{0,"+f'{len_entry}'+r"}$)"
            else:
                regex = r"(^$)"
        Validating.matchTest(parameter, regex, is_nome)
    
    def real(parameter, len_entry, can_be_negative=False):
        is_nome = False
        if can_be_negative is True:
            if len_entry is None:
                regex = r"^(\-{0,1})((\d*)|(\d+((\.{0,1})|(\,{0,1})))(\d*))$"
            elif type(len_entry) is int:
                regex = r"^(\-{0,1})((\d*)|(\d+((\.{0,1})|(\,{0,1})))(\d{0,"+f'{len_entry}'+r"}))$"
            elif type(len_entry) is tuple and len(len_entry) == 2:
                regex = r"^(\-{0,1})((\d{0,"+f'{len_entry[0]}'+r"})|(\d{1,"+f'{len_entry[0]}'+r"}((\.{0,1})|(\,{0,1})))|(\d{1,"+f'{len_entry[0]}'+r"}((\.)|(\,)))(\d{0,"+f'{len_entry[1]}'+r"}))$"
                # Caller().info(text='Verificar o regex depois, precisei colocar um -1 que não faz sentido para funcionar')
            else:
                regex = r"(^$)"
        else:
            if len_entry is None:
                regex = r"^((\d*)|(\d+((\.{0,1})|(\,{0,1})))(\d*))$"
            elif type(len_entry) is int:
                regex = r"^((\d*)|(\d+((\.{0,1})|(\,{0,1})))(\d{0,"+f'{len_entry}'+r"}))$"
            elif type(len_entry) is tuple and len(len_entry) == 2:
                regex = r"^((\d{0,"+f'{len_entry[0]}'+r"})|(\d{1,"+f'{len_entry[0]}'+r"}((\.{0,1})|(\,{0,1})))|(\d{1,"+f'{len_entry[0]}'+r"}((\.)|(\,)))(\d{0,"+f'{len_entry[1]}'+r"}))$"
                # Caller().info(text='Verificar o regex depois, precisei colocar um -1 que não faz sentido para funcionar')
            else:
                regex = r"(^$)"
        Validating.matchTest(parameter, regex, is_nome)
    
    def words(parameter, len_entry):
        is_nome = True
        if len_entry is None:
            regex = r"^([a-z]\s?)*$"
        elif type(len_entry) is int:
            regex = r"^([a-z]){0,"+f'{len_entry}'+r"}$"
        else:
            regex = r"(^$)"
        Validating.matchTest(parameter, regex, is_nome)