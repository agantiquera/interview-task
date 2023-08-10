from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!

    request_id = request.args.get('id')
    request_name = request.args.get('name')
    request_age = request.args.get('age')
    request_occupation = request.args.get('occupation')

    request_input = [
        {'request_id': request_id},
        {'request_name': request_name},
        {'request_age': request_age},
        {'request_occupation': request_occupation}
    ]
    
    names = [
        "John Doe", "Jane Doe", "Joe Doe", "John Smith", "Jane Smith", "Joe Smith"
    ]
    search_name = [
        "John", "Jane", "Joe", "Doe", "Smith"
    ]
    occupation = [
        "developer", "engineer", "designer", "architect", "manager", "designer"
    ]

    parameters_result = []


    for item in USERS:
        if request_id != None:  
            if item['id'] == request_id:
                found_id = item
                if found_id:
                    parameters_result += [found_id]

        if request_name != None:
            split_request_name = request_name.split()
            cap_name = [capi.capitalize() for capi in split_request_name]
            str_name = " ".join(str(name1) for name1 in cap_name)
            similar_names = [sim_name for sim_name in names if 
                             any(names in str_name in sim_name for names in search_name )]
            for result_name in similar_names:
                if item['name'] == result_name:
                    found_name = item
                    if found_name:
                        parameters_result += [found_name]
                        

        if request_age != None:
            if item['age'] == int(request_age):
                found_age = item
                if found_age:
                    parameters_result += [found_age]
        
        if request_occupation != None:
            similar_occ = [sim_occ for sim_occ in occupation if request_occupation in sim_occ]
            return similar_occ
            #occ1 = None      

            # for occ in similar_occ:
            #      if item['occupation'] == occ.capitalize():
            #          found_occ = item
                     #parameters_result += found_occ

    new_parameters_result = []

    for param in range(len(parameters_result)):
        if parameters_result[param] not in parameters_result[param+1:]:
            new_parameters_result.append(parameters_result[param])

    
    return new_parameters_result
        

