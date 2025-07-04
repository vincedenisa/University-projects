#pragma once

#include <exception>
#include <string>
#include <utility>

class BaseException : public std::exception {
protected:
    const std::string exception_msg;
public:
    BaseException() = default;

    explicit BaseException(std::string msg) : exception_msg(std::move(msg)) {}

    virtual const char *what() { return this->exception_msg.c_str(); }
};


class DynamicArrayException : public BaseException {
public:
    DynamicArrayException() = default;

    explicit DynamicArrayException(std::string msg) : BaseException{std::move(msg)} {};
};


class RepositoryException : public BaseException {
public:
    RepositoryException() = default;

    explicit RepositoryException(std::string msg) : BaseException{std::move(msg)} {};
};


class ValidationException : public BaseException {
public:
    ValidationException() = default;

    explicit ValidationException(std::string msg) : BaseException{std::move(msg)} {};
};


class ServiceException : public BaseException {
public:
    ServiceException() = default;

    explicit ServiceException(std::string msg) : BaseException{std::move(msg)} {};
};

