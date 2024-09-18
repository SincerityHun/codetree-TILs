#include <iostream>
#include <vector>
#include <math.h>

#define MAX_ID 100001

typedef long long LL;

using namespace std;

// 색깔 트리 = 다양한 색의 노드
int parent_id[MAX_ID];                // parent_id[m_id] = p_id;
int color_id[MAX_ID];                 // color_id[m_id] = color;
int depth_id[MAX_ID];                 //  depth_id[m_id] = depth count;
vector<vector<int>> child_id(MAX_ID); // child_id[m_id] = [child_id,,,,]
int subtree_color[MAX_ID][5];         // subtree_color[m_id가 루트인 서브트리] = [1,0,0,0,0]
vector<int> root_id;                  // root id 모아 놓음
bool check_depth(int next_id, int cur_count, int goal_id)
{
    // cur_count랑 depth_id를 비교
    // cur_count랑 같다면 -> depth roll back  돌리기
    //cout << "CHECKDEPTH: " << next_id << " " << goal_id << endl; //TEST
    if (cur_count < depth_id[next_id])
    {
        if (parent_id[next_id] == -1)
            return true;
        return check_depth(parent_id[next_id], cur_count+1, goal_id);
    }
    return false;
}
void subtree_update(int next_id, int cur_color)
{
    subtree_color[next_id][cur_color - 1] += 1;
    if (parent_id[next_id] == -1)
        return;
    return subtree_update(parent_id[next_id], cur_color);
}
void add_node(int m_id, int p_id, int color, int max_depth)
{
    // cout << "ADD" << endl;
    // p_id가 -1이면 루트임
    if (p_id == -1)
    {
        parent_id[m_id] = -1;
        color_id[m_id] = color - 1; //  0~4로 저장
        depth_id[m_id] = max_depth;
        subtree_color[m_id][color - 1] = 1;
        root_id.emplace_back(m_id);
        return;
    }
    // depth 검사
    if (check_depth(p_id, 1, m_id))
    {
        subtree_update(p_id, color);
        parent_id[m_id] = p_id;
        color_id[m_id] = color - 1;
        depth_id[m_id] = max_depth;
        subtree_color[m_id][color - 1] = 1;
        child_id[p_id].emplace_back(m_id);
        return;
    }
    return;
}
void down_color(int m_id, int color)
{

    color_id[m_id] = color - 1;
    // subtree_id을 확인하면 전체 노드 확인 가능
    int result = 0;
    for (int i = 0; i < 5; ++i)
    {
        result += subtree_color[m_id][i];
        subtree_color[m_id][i] = 0;
    }
    // 그 수를 color-1칸에 넣어
    subtree_color[m_id][color - 1] = result;
    // child_node 돌면서 down_color
    for (auto item : child_id[m_id])
    {
        down_color(item, color);
    }
}
void up_color(int id, int result[], int color, int num)
{
    for (int i = 0; i < 5; ++i)
    {
        subtree_color[id][i] -= result[i];
    }
    subtree_color[id][color - 1] += num;
    if (parent_id[id] == -1)
        return;
    up_color(parent_id[id], result, color, num);
}
void change_color(int m_id, int color)
{
    // 2. 색깔 변경
    // 특정 m_id를 루트로 하는 서브트리의 모든 노드의 색깔을 color로 변경
    // 50000번
    // cout << "CHANGE" << endl; // TEST
    int result[5];
    int num = 0;
    for (int i = 0; i < 5; ++i)
    {
        result[i] = subtree_color[m_id][i];
        num += result[i];
    }
    // 얘를 기점으로 아래로 ㄱ
    down_color(m_id, color);
    // p_id을 기점으로 위로 ㄱ
    if (parent_id[m_id] != -1)
        up_color(parent_id[m_id], result, color, num);
}
int get_color(int m_id)
{
    // 3. 색깔 조회
    // cout << "GET" << endl; // TEST
    // 특정 m_id의 현재 색깔 조회 -> O(1)
    // 200000번
    return color_id[m_id] + 1;
}
LL _count_color(int roots)
{
    // cout << "root: " << roots; // TEST
    int tmp_count = 0;
    for (int i = 0; i < 5; ++i)
        if (subtree_color[roots][i] != 0)
            ++tmp_count;
    LL results = pow(tmp_count, 2);
    // cout << " " << results << endl; // TEST
    for (auto item : child_id[roots])
    {
        // cout << "kids: " << item << endl;
        results += _count_color(item);
    }
    return results;
}
LL count_color()
{
    // 4. 점수 조회
    // 모든 노드의 가치 제곱의 합
    // 특정 노드의 가치 = 해당 노드를 루트로 하는 서브트리 내 서로 다른 색깔의 수
    // 100번
    // cout << "COUNT" << endl; // TEST
    LL result = 0;
    for (auto roots : root_id)
    {
        result += _count_color(roots);
    }
    return result;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    //freopen("input.txt", "r", stdin);

    int Q;         // 명령의 수 Q (1~1e+5)
    int choice;    // 명령어 100, 200, 300, 400
    int m_id;      // 해당 노드 id 1~1e+5
    int p_id;      // 부모 노드 id -1, 1~1e+5
    int color;     // 색 빨주노초파 1~5
    int max_depth; // 최대 깊이 1~100

    cin >> Q;
    for (int test_case = 1; test_case <= Q; ++test_case)
    {
        cin >> choice;
        switch (choice)
        {
        case 100: // 노드 추가
            cin >> m_id >> p_id >> color >> max_depth;
            add_node(m_id, p_id, color, max_depth);
            break;
        case 200: // 색깔 변경
            cin >> m_id >> color;
            change_color(m_id, color);
            break;
        case 300: // 색깔 조회
            cin >> m_id;
            cout << get_color(m_id) << endl;
            break;
        default: // 점수 조 회
            cout << count_color() << endl;
            break;
        }
    }

    return 0;
}