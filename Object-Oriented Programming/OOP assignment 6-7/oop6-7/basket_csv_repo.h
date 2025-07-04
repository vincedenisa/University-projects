#pragma once
#include "basket_file_repo.h"

class BasketCSVRepo : public BasketFileRepo {
protected:
    void read_from_file() override;

    void write_to_file() override;

public:
    explicit BasketCSVRepo(std::string &file_name);
};


