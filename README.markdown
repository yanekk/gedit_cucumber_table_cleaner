Introduction
============

Cucumber Table Cleaner is a Gedit/Gmate plugin for cleaning up every table within cucumber features, in this example:

      Scenario Outline: Show or hide edit profile link
        Given the following user records
          |username|password|admin|
          |bob|secret|false|
          |admin|secret|true|
        Given I am logged in as "<login>" with password "secret"
        When I visit profile for "<profile>"
        Then I should <action>

        Examples:
          |login|profile| action|
          |admin|bob|see "Edit Profile"|
          |bob|bob| see "Edit Profile"|
          ||bob|not see "Edit Profile"|
          |bob|admin|not see "Edit Profile"|

*Example taken from http://railscasts.com/episodes/159-more-on-cucumber*

By selecting desired table and clicking Ctrl + Shift + | , table became easier to read:

      Scenario Outline: Show or hide edit profile link
        Given the following user records
          | username | password | admin |
          |   bob    |  secret  | false |
          |  admin   |  secret  |  true |
        Given I am logged in as "<login>" with password "secret"
        When I visit profile for "<profile>"
        Then I should <action>

        Examples:
          | login | profile |         action         |
          | admin |   bob   |   see "Edit Profile"   |
          |  bob  |   bob   |   see "Edit Profile"   |
          |       |   bob   | not see "Edit Profile" |
          |  bob  |  admin  | not see "Edit Profile" |

Installation
============
1. Ensure gedit is installed
2. Fetch plugin from git repository
    *   `git clone git://github.com/yanekk/gedit_cucumber_table_cleaner.git`
3. Install it with installation script
    *   `cd gedit_cucumber_table_cleaner`
    *   `./install.sh`
4. Select plugin's checkbox in gedit's Preferences window
5. Have fun with cleaning up cucumber tables

