#pragma once

class AbstractFilter {
    public:
        virtual bool include(const TrenchCoat &t) const = 0;
};

