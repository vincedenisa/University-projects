#pragma once


#include "trench_coat.h"

class TrenchCoatValidator {
public:
    /*
        Validate the attributes of a created trench coat.
        Throws: ValidationException if any of the trench coat attributes are invalid.
     */
    static void validate(TrenchCoat &t);
};


