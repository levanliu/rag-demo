#include <cstdio>
#include <string>
#include <memory>

std::string query_db(const std::string& question) {
    std::string cmd = "uv run query_wrapper.py \"" + question + "\"";
    std::string result;
    char buffer[128];
    
    FILE* pipe = popen(cmd.c_str(), "r");
    if (!pipe) {
        return "Error";
    }
    
    while (fgets(buffer, sizeof(buffer), pipe) != nullptr) {
        result += buffer;
    }
    
    pclose(pipe);
    return result;
}

int main()
{
    std::string question = "令狐冲领悟了什么魔法？";
    std::string answer = query_db(question);
    printf("Answer: %s\n", answer.c_str());
    return 0;
}