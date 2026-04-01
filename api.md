# V1

Types:

```python
from everos.types import V1QueryTaskStatusResponse
```

Methods:

- <code title="get /api/v1/tasks/{task_id}">client.v1.<a href="./src/everos/resources/v1/v1.py">query_task_status</a>(task_id) -> <a href="./src/everos/types/v1_query_task_status_response.py">V1QueryTaskStatusResponse</a></code>

## Memories

Types:

```python
from everos.types.v1 import (
    AddResponse,
    ContentItem,
    FlushResponse,
    MemoryGetResponse,
    MemorySearchResponse,
)
```

Methods:

- <code title="post /api/v1/memories">client.v1.memories.<a href="./src/everos/resources/v1/memories/memories.py">create</a>(\*\*<a href="src/everos/types/v1/memory_create_params.py">params</a>) -> <a href="./src/everos/types/v1/add_response.py">AddResponse</a></code>
- <code title="post /api/v1/memories/delete">client.v1.memories.<a href="./src/everos/resources/v1/memories/memories.py">delete</a>(\*\*<a href="src/everos/types/v1/memory_delete_params.py">params</a>) -> None</code>
- <code title="post /api/v1/memories/flush">client.v1.memories.<a href="./src/everos/resources/v1/memories/memories.py">flush</a>(\*\*<a href="src/everos/types/v1/memory_flush_params.py">params</a>) -> <a href="./src/everos/types/v1/flush_response.py">FlushResponse</a></code>
- <code title="post /api/v1/memories/get">client.v1.memories.<a href="./src/everos/resources/v1/memories/memories.py">get</a>(\*\*<a href="src/everos/types/v1/memory_get_params.py">params</a>) -> <a href="./src/everos/types/v1/memory_get_response.py">MemoryGetResponse</a></code>
- <code title="post /api/v1/memories/search">client.v1.memories.<a href="./src/everos/resources/v1/memories/memories.py">search</a>(\*\*<a href="src/everos/types/v1/memory_search_params.py">params</a>) -> <a href="./src/everos/types/v1/memory_search_response.py">MemorySearchResponse</a></code>

### Group

Methods:

- <code title="post /api/v1/memories/group">client.v1.memories.group.<a href="./src/everos/resources/v1/memories/group.py">create</a>(\*\*<a href="src/everos/types/v1/memories/group_create_params.py">params</a>) -> <a href="./src/everos/types/v1/add_response.py">AddResponse</a></code>
- <code title="post /api/v1/memories/group/flush">client.v1.memories.group.<a href="./src/everos/resources/v1/memories/group.py">flush</a>(\*\*<a href="src/everos/types/v1/memories/group_flush_params.py">params</a>) -> <a href="./src/everos/types/v1/flush_response.py">FlushResponse</a></code>

### Agent

Methods:

- <code title="post /api/v1/memories/agent">client.v1.memories.agent.<a href="./src/everos/resources/v1/memories/agent.py">create</a>(\*\*<a href="src/everos/types/v1/memories/agent_create_params.py">params</a>) -> <a href="./src/everos/types/v1/add_response.py">AddResponse</a></code>
- <code title="post /api/v1/memories/agent/flush">client.v1.memories.agent.<a href="./src/everos/resources/v1/memories/agent.py">flush</a>(\*\*<a href="src/everos/types/v1/memories/agent_flush_params.py">params</a>) -> <a href="./src/everos/types/v1/flush_response.py">FlushResponse</a></code>

## Groups

Types:

```python
from everos.types.v1 import GroupAPIResponse
```

Methods:

- <code title="get /api/v1/groups/{group_id}">client.v1.groups.<a href="./src/everos/resources/v1/groups.py">retrieve</a>(group_id) -> <a href="./src/everos/types/v1/group_api_response.py">GroupAPIResponse</a></code>
- <code title="patch /api/v1/groups/{group_id}">client.v1.groups.<a href="./src/everos/resources/v1/groups.py">update</a>(group_id, \*\*<a href="src/everos/types/v1/group_update_params.py">params</a>) -> <a href="./src/everos/types/v1/group_api_response.py">GroupAPIResponse</a></code>
- <code title="post /api/v1/groups">client.v1.groups.<a href="./src/everos/resources/v1/groups.py">create_or_update</a>(\*\*<a href="src/everos/types/v1/group_create_or_update_params.py">params</a>) -> <a href="./src/everos/types/v1/group_api_response.py">GroupAPIResponse</a></code>

## Senders

Types:

```python
from everos.types.v1 import SenderAPIResponse
```

Methods:

- <code title="get /api/v1/senders/{sender_id}">client.v1.senders.<a href="./src/everos/resources/v1/senders.py">retrieve</a>(sender_id) -> <a href="./src/everos/types/v1/sender_api_response.py">SenderAPIResponse</a></code>
- <code title="patch /api/v1/senders/{sender_id}">client.v1.senders.<a href="./src/everos/resources/v1/senders.py">update</a>(sender_id, \*\*<a href="src/everos/types/v1/sender_update_params.py">params</a>) -> <a href="./src/everos/types/v1/sender_api_response.py">SenderAPIResponse</a></code>
- <code title="post /api/v1/senders">client.v1.senders.<a href="./src/everos/resources/v1/senders.py">create_or_update</a>(\*\*<a href="src/everos/types/v1/sender_create_or_update_params.py">params</a>) -> <a href="./src/everos/types/v1/sender_api_response.py">SenderAPIResponse</a></code>

## Object

Types:

```python
from everos.types.v1 import ObjectGetPresignedURLResponse
```

Methods:

- <code title="post /api/v1/object/sign">client.v1.object.<a href="./src/everos/resources/v1/object.py">get_presigned_url</a>(\*\*<a href="src/everos/types/v1/object_get_presigned_url_params.py">params</a>) -> <a href="./src/everos/types/v1/object_get_presigned_url_response.py">ObjectGetPresignedURLResponse</a></code>

## Settings

Types:

```python
from everos.types.v1 import LlmProviderConfig, SettingsAPIResponse
```

Methods:

- <code title="get /api/v1/settings">client.v1.settings.<a href="./src/everos/resources/v1/settings.py">retrieve</a>() -> <a href="./src/everos/types/v1/settings_api_response.py">SettingsAPIResponse</a></code>
- <code title="put /api/v1/settings">client.v1.settings.<a href="./src/everos/resources/v1/settings.py">update</a>(\*\*<a href="src/everos/types/v1/setting_update_params.py">params</a>) -> <a href="./src/everos/types/v1/settings_api_response.py">SettingsAPIResponse</a></code>
