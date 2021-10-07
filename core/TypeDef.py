main_type_defs = ''' 
schema {
query: Query
subscription: Subscription
mutation: Mutation
}

type Query {
_unused: Boolean 
}

type Mutation {
_unused: Boolean 
}

type Subscription {
_unused: Boolean
}
'''

type_defs = [main_type_defs]


def AddTypeDef(newTypeDef):
    if type(newTypeDef).__name__ == 'list':
        for i in newTypeDef:
            type_defs.append(i)
    else:
        type_defs.append(newTypeDef)
