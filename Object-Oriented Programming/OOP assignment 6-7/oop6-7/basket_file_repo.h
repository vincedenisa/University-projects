#pragma once

#include "file_repo.h"

class BasketFileRepo : public FileRepo {
public:
    explicit BasketFileRepo(std::string &file_name);

    void add_trench_to_repo(const TrenchCoat &t) override;

    int count_same_coat_in_repo(const TrenchCoat &t);
};


