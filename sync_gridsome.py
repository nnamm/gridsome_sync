""" pyftpsyncライブラリを使用し、Gridsomeでビルドしたデータ（dist/）をデプロイ先と同期する """

import configparser
import logging.handlers

from ftpsync.ftp_target import FtpTarget
from ftpsync.targets import FsTarget
from ftpsync.synchronizers import BiDirSynchronizer
from ftpsync.util import set_pyftpsync_logger


def sync_gridsome() -> None:
    """
    指定のローカルとリモートディレクトリを同期する
    """

    cfg = configparser.ConfigParser()
    cfg.read("config.ini")

    # ローカルとリモートの設定
    local = FsTarget(cfg["PATH"]["LOCAL"])
    user = cfg["FTPS"]["USER"]
    passwd = cfg["FTPS"]["PASSWORD"]
    remote = FtpTarget(
        cfg["PATH"]["REMOTE"],  # リモートディレクトリパス
        cfg["FTPS"]["SERVER"],  # FTPサーバ
        username=user,
        password=passwd,
        tls=True,  # FTPS有効
    )

    # オプション設定
    # ローカル優先／--deleteオプション有効／指定ディレクトリは同期除外
    opts = {"resolve": "local", "delete": True, "force": True}

    # 同期の実行
    sync = BiDirSynchronizer(local, remote, opts)
    sync.run()


if __name__ == "__main__":
    # ロガーの設定
    # pyftpsync.logにログを残す
    logger = logging.getLogger("sync.gridsome")
    log_path = "./pyftpsync.log"
    handler = logging.handlers.WatchedFileHandler(log_path)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    set_pyftpsync_logger(logger)

    # 同期
    sync_gridsome()
