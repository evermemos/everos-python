# V1

## Groups

Types:

```python
from everos.types.v1 import CreateGroupRequest, GroupAPIResponse, GroupResponse, PatchGroupRequest
```

Methods:

- <code title="post /api/v1/groups">client.v1.groups.<a href="./src/everos/resources/v1/groups.py">create</a>(\*\*<a href="src/everos/types/v1/group_create_params.py">params</a>) -> <a href="./src/everos/types/v1/group_api_response.py">GroupAPIResponse</a></code>
- <code title="get /api/v1/groups/{group_id}">client.v1.groups.<a href="./src/everos/resources/v1/groups.py">retrieve</a>(group_id) -> <a href="./src/everos/types/v1/group_api_response.py">GroupAPIResponse</a></code>
- <code title="patch /api/v1/groups/{group_id}">client.v1.groups.<a href="./src/everos/resources/v1/groups.py">patch</a>(group_id, \*\*<a href="src/everos/types/v1/group_patch_params.py">params</a>) -> <a href="./src/everos/types/v1/group_api_response.py">GroupAPIResponse</a></code>

## Settings

Types:

```python
from everos.types.v1 import (
    LlmCustomSetting,
    LlmProviderConfig,
    SettingsAPIResponse,
    SettingsResponse,
    UpdateSettingsRequest,
)
```

Methods:

- <code title="get /api/v1/settings">client.v1.settings.<a href="./src/everos/resources/v1/settings.py">retrieve</a>() -> <a href="./src/everos/types/v1/settings_api_response.py">SettingsAPIResponse</a></code>
- <code title="put /api/v1/settings">client.v1.settings.<a href="./src/everos/resources/v1/settings.py">update</a>(\*\*<a href="src/everos/types/v1/setting_update_params.py">params</a>) -> <a href="./src/everos/types/v1/settings_api_response.py">SettingsAPIResponse</a></code>

## Senders

Types:

```python
from everos.types.v1 import (
    CreateSenderRequest,
    PatchSenderRequest,
    SenderAPIResponse,
    SenderResponse,
)
```

Methods:

- <code title="post /api/v1/senders">client.v1.senders.<a href="./src/everos/resources/v1/senders.py">create</a>(\*\*<a href="src/everos/types/v1/sender_create_params.py">params</a>) -> <a href="./src/everos/types/v1/sender_api_response.py">SenderAPIResponse</a></code>
- <code title="get /api/v1/senders/{sender_id}">client.v1.senders.<a href="./src/everos/resources/v1/senders.py">retrieve</a>(sender_id) -> <a href="./src/everos/types/v1/sender_api_response.py">SenderAPIResponse</a></code>
- <code title="patch /api/v1/senders/{sender_id}">client.v1.senders.<a href="./src/everos/resources/v1/senders.py">patch</a>(sender_id, \*\*<a href="src/everos/types/v1/sender_patch_params.py">params</a>) -> <a href="./src/everos/types/v1/sender_api_response.py">SenderAPIResponse</a></code>

## Memories

Types:

```python
from everos.types.v1 import (
    AddResponse,
    AddResult,
    AsyncAddResponse,
    AsyncAddResult,
    ContentItem,
    DeleteMemoriesRequest,
    EpisodeItem,
    FlushResponse,
    FlushResult,
    GetMemRequest,
    GetMemResponse,
    GetMemoriesResponse,
    MessageItem,
    PersonalAddRequest,
    PersonalFlushRequest,
    ProfileItem,
    RawMessageDto,
    SearchMemoriesRequest,
    SearchMemoriesResponse,
    SearchMemoriesResponseData,
)
```

Methods:

- <code title="post /api/v1/memories/delete">client.v1.memories.<a href="./src/everos/resources/v1/memories/memories.py">delete</a>(\*\*<a href="src/everos/types/v1/memory_delete_params.py">params</a>) -> None</code>
- <code title="post /api/v1/memories">client.v1.memories.<a href="./src/everos/resources/v1/memories/memories.py">add</a>(\*\*<a href="src/everos/types/v1/memory_add_params.py">params</a>) -> <a href="./src/everos/types/v1/add_response.py">AddResponse</a></code>
- <code title="post /api/v1/memories/flush">client.v1.memories.<a href="./src/everos/resources/v1/memories/memories.py">flush</a>(\*\*<a href="src/everos/types/v1/memory_flush_params.py">params</a>) -> <a href="./src/everos/types/v1/flush_response.py">FlushResponse</a></code>
- <code title="post /api/v1/memories/get">client.v1.memories.<a href="./src/everos/resources/v1/memories/memories.py">get</a>(\*\*<a href="src/everos/types/v1/memory_get_params.py">params</a>) -> <a href="./src/everos/types/v1/get_memories_response.py">GetMemoriesResponse</a></code>
- <code title="post /api/v1/memories/search">client.v1.memories.<a href="./src/everos/resources/v1/memories/memories.py">search</a>(\*\*<a href="src/everos/types/v1/memory_search_params.py">params</a>) -> <a href="./src/everos/types/v1/search_memories_response.py">SearchMemoriesResponse</a></code>

### Agent

Types:

```python
from everos.types.v1.memories import (
    AgentAddRequest,
    AgentCaseItem,
    AgentFlushRequest,
    AgentMessageItem,
    AgentSkillItem,
    ToolCall,
    ToolCallFunction,
)
```

Methods:

- <code title="post /api/v1/memories/agent">client.v1.memories.agent.<a href="./src/everos/resources/v1/memories/agent.py">add</a>(\*\*<a href="src/everos/types/v1/memories/agent_add_params.py">params</a>) -> <a href="./src/everos/types/v1/add_response.py">AddResponse</a></code>
- <code title="post /api/v1/memories/agent/flush">client.v1.memories.agent.<a href="./src/everos/resources/v1/memories/agent.py">flush</a>(\*\*<a href="src/everos/types/v1/memories/agent_flush_params.py">params</a>) -> <a href="./src/everos/types/v1/flush_response.py">FlushResponse</a></code>

### Group

Types:

```python
from everos.types.v1.memories import GroupAddRequest, GroupFlushRequest, GroupMessageItem
```

Methods:

- <code title="post /api/v1/memories/group">client.v1.memories.group.<a href="./src/everos/resources/v1/memories/group.py">add</a>(\*\*<a href="src/everos/types/v1/memories/group_add_params.py">params</a>) -> <a href="./src/everos/types/v1/add_response.py">AddResponse</a></code>
- <code title="post /api/v1/memories/group/flush">client.v1.memories.group.<a href="./src/everos/resources/v1/memories/group.py">flush</a>(\*\*<a href="src/everos/types/v1/memories/group_flush_params.py">params</a>) -> <a href="./src/everos/types/v1/flush_response.py">FlushResponse</a></code>

## Object

Types:

```python
from everos.types.v1 import (
    ObjectSignItem,
    ObjectSignItemRequest,
    ObjectSignRequest,
    ObjectSignResponse,
    ObjectSignedInfo,
)
```

Methods:

- <code title="post /api/v1/object/sign">client.v1.object.<a href="./src/everos/resources/v1/object.py">sign</a>(\*\*<a href="src/everos/types/v1/object_sign_params.py">params</a>) -> <a href="./src/everos/types/v1/object_sign_response.py">ObjectSignResponse</a></code>

## Tasks

Types:

```python
from everos.types.v1 import GetTaskStatusResponse, TaskStatusResult
```

Methods:

- <code title="get /api/v1/tasks/{task_id}">client.v1.tasks.<a href="./src/everos/resources/v1/tasks.py">retrieve</a>(task_id) -> <a href="./src/everos/types/v1/get_task_status_response.py">GetTaskStatusResponse</a></code>
