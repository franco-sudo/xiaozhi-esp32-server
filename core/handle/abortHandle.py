import json
import logging

logger = logging.getLogger(__name__)


async def handleAbortMessage(conn):
    logger.info("Abort message received")
    # 设置成打断状态，会自动打断llm、tts任务
    conn.client_abort = True
    # 打断屏显任务
    conn.stop_all_tasks()
    # 打断客户端说话状态
    await conn.websocket.send(json.dumps({"type": "tts", "state": "stop", "session_id": conn.session_id}))
    conn.clearSpeakStatus()
    logger.info("Abort message received-end")
