#pragma once

#include "basket_file_repo.h"

class BasketHTMLRepo : public BasketFileRepo {
protected:
    void read_from_file() override;

    void write_to_file() override;

public:
    explicit BasketHTMLRepo(std::string &file_name);
};


